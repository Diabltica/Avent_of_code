#include "days.h"
#include <stdio.h>

int main()
{

	int count = 0;


	count = sonar_Sweep_part1();
	printf("Part 1 %d\n", count);
	count = sonar_Sweep_part2();
	printf("Part 2 %d", count);
	return 0;
}
