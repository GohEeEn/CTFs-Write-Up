#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int generatePin() {

    // Time constant given constructed in `struct tm`
    struct tm now = {
	.tm_sec=45,
	.tm_min=23,
	.tm_hour=11,
	.tm_mon=0,
	.tm_year=130,
	.tm_mday=1
    };

    // Convert to UTC time / GMT
    // Ref : https://www.man7.org/linux/man-pages/man3/timegm.3.html
    time_t current = timegm(&now);
    
    printf("[Seconds since EPOCH] %lld s - PIN : ", current);
    
    srand(current);
    return rand();
}

int main()
{
    printf("%d\n", generatePin());
    return 0;
}