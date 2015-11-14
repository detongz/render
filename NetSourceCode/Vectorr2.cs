using System;

namespace BzPoints
{
	public class Vectorr2
	{
		public Vectorr2(float x, float y)
		{
			this.x = x;
			this.y = y;
		}
		public float x;
		public float y;
		public static Vectorr2 operator +(Vectorr2 now, Vectorr2 target)
		{
			return new Vectorr2(now.x + target.x, now.y + target.y);
		}
		public static Vectorr2 operator *(float target, Vectorr2 target2)
		{
			return new Vectorr2(target2.x * target, target2.y * target);
		}
		public override string ToString()
		{
			return "x=" + x + "  y=" + y;
		}
	}
}
