#include<stdio.h>

int main(void)
{
	int dice_1[6];
	int dice_2[6];

	scanf("%d %d %d %d %d %d", dice_1[0], dice_1[1], dice_1[2], dice_1[3], dice_1[4], dice_1[5]);
	scanf("%d %d %d %d %d %d", dice_2[0], dice_2[1], dice_2[2], dice_2[3], dice_2[4], dice_2[5]);

	int prob = 0;

	for(int i = 0 ; i < 6 ; i++) {

		for(int j = 0 ; j < 6 ; j++) {

			if(dice_1[i] > dice_2[j]) {

				prob++;
			}
		}
	}


	return 0;
}