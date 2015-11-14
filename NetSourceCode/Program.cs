using System; 
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace BzPoints
{
	class Program
	{
		static TcpListener listener;
		static int port;
		static IPAddress ip;
		static void Main()
		{
			listener = new TcpListener(ip,port);
			while(true)
			{
				TcpClient client=listener.AcceptTcpClient();
				while(true)
				{
					if(client.Available!=0)
					{
						byte[] buffer=new byte[client.GetStream().Length];
						client.GetStream().Read(buffer, 0, buffer.Length);
						string data = Encoding.UTF8.GetString(buffer);
						string[] args = data.Split('|');
						if (args.Length < 1) { client.Close(); break; }
						List<Vector2> points = new List<Vector2>();
						string[] pointsStr = args[0].Split(';');
						for (int a = 0; a < pointsStr.Length - 1; a++)
						{
							points.Add(new Vector2(float.Parse(pointsStr[a].Split('|')[0]), float.Parse(pointsStr[a].Split('|')[1])));
						}
						List<Vector2> results = GetSmoothPoint(points, float.Parse(args[1]), args[2] == "1" ? true : false);
						string valu = "";
						foreach (Vector2 ve in results)
						{
							valu += ve.x + "|" + ve.y + ";";
						}
						byte[] rsu = Encoding.UTF8.GetBytes(valu);
						client.GetStream().Write(rsu, 0, rsu.Length);
						client.GetStream().Flush();
						client.Close();
						break;
					}
				}
			}
		}
		static public List<Vector2> GetSmoothPoint(List<Vector2> targetArray, float precision, bool headtotial = true)
		{
			//1.获取采样点
			if (precision == 1) { return targetArray; }
			List<Vectorr2> samplePoint = new List<Vectorr2>();
			int samcount = (int)((float)targetArray.Count * precision);
			int interval = targetArray.Count / samcount;
			for (int sam = 0; sam < samcount; sam++)
			{
				Vector2 get = targetArray[sam * interval];
				samplePoint.Add(new Vectorr2(get.x, get.y));
			}
			samplePoint.Add(new Vectorr2(targetArray[targetArray.Count - 1].x, targetArray[targetArray.Count - 1].y));
			//2.从采样点开始对用户画的点数据进行重采样
			List<Vector2> tempToGl = new List<Vector2>();//准备交给Gl的数据
			int glCount = targetArray.Count;
			float inter = 1.0f / (float)glCount;
			for (float a = 0; a < 1; )
			{
				Vectorr2[] test1 = new Vectorr2[samcount + 1];
				samplePoint.CopyTo(test1);
				Vectorr2 myV = GetBezierPoint(test1, a);
				tempToGl.Add(new Vector2(myV.x, myV.y));
				a += inter;
			}
			//3.将重建的点数据处理并交给Gl
			if (headtotial)
				tempToGl[tempToGl.Count - 1] = tempToGl[0];
			return tempToGl;
			//结束平滑代码
		}
		static public Vectorr2 GetBezierPoint(Vectorr2[] pointList, float t)//t从0-1
		{
			int count = GetCount(pointList);
			if (count == 1)
			{
				return pointList[0];
			}
			else
			{
				for (int a = 0; a < count - 1; a++)
				{
					pointList[a] = (1 - t) * pointList[a] + t * pointList[a + 1];
				}
				pointList[count - 1] = null;
				return GetBezierPoint(pointList, t);
			}
		}

		static public int GetCount(Vectorr2[] list)
		{
			int count = 0;
			for (int a = 0; a < list.Length; a++)
			{
				if (list[a] != null) count++;
			}
			return count;
		}
	}
}
