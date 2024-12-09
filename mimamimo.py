#include <stdio.h>
#include <math.h>

int main() {
    float r, h;
    const float PI = 3.14;

    // Nhập bán kính và chiều cao từ bàn phím
    printf("Nhap ban kinh day (r): ");
    scanf("%f", &r);
    printf("Nhap chieu cao (h): ");
    scanf("%f", &h);

    // Tính diện tích xung quanh
    float dienTichXungQuanh = 2 * PI * r * h;
    // Tính diện tích toàn phần
    float dienTichToanPhan = 2 * PI * r * (r + h);
    // Tính thể tích
    float theTich = PI * r * r * h;

    // In kết quả, làm tròn đến số thập phân thứ hai
    printf("Dien tich xung quanh: %.2f\n", roundf(dienTichXungQuanh * 100) / 100);
    printf("Dien tich toan phan: %.2f\n", roundf(dienTichToanPhan * 100) / 100);
    printf("The tich: %.2f\n", roundf(theTich * 100) / 100);

    return 0;
}
