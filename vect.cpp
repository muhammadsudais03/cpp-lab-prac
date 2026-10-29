// #include <iostream>
// using namespace std;

// int main() {
//     int marks;
//     cout << "Enter marks: ";
//     cin >> marks;

//     if (marks >= 50) {
//         cout << "Pass";
//     }
//     else {
//         cout << "Fail";
//     }

//     return 0;
// }

// TASK # 02

// #include <iostream>
// using namespace std;

// int main() {
//     int num;
//     cout << "Enter a number: ";
//     cin >> num;

//     if (num % 2 == 0) {
//         cout << "Even";
//     }
//     else {
//         cout << "Odd";
//     }

//     return 0;
// }

// TASK # 03

// #include <iostream>
// using namespace std;

// int main() {
//     int a, b;
//     cout << "Enter two numbers: ";
//     cin >> a >> b;

//     if (a > b) {
//         cout << a << " is larger";
//     }
//     else if (b > a) {
//         cout << b << " is larger";
//     }
//     else {
//         cout << "Both numbers are equal";
//     }

//     return 0;
// }

// TASK # 04
// USING FOR LOOP
// #include <iostream>
// using namespace std;

// int main() {
//     for (int i = 1; i <= 20; i++) {
//         cout << i << endl;
//     }

//     return 0;
// }

// USING WHILE LOOP

// #include <iostream>
// using namespace std;

// int main() {
//     int i = 1;

//     while (i <= 20) {
//         cout << i << endl;
//         i++;
//     }

//     return 0;
// }

// TASK # 05

// #include <iostream>
// using namespace std;

// int main() {
//     for (int i = 1; i <= 5; i++) {
//         for (int j = 1; j <= i; j++) {
//             cout << "*";
//         }
//         cout << endl;
//     }

//     return 0;
// }
#include <iostream> 
using namespace std;
int main() {
int arr[5] = {5, 3, 8, 1, 2};
 
int n = 5;	
// Find Max and Min
int max = arr[0], min = arr[0];
 for (int i = 1; i < n; i++) {
if (arr[i] > max) 
max = arr[i];
if (arr[i] < min)
 min = arr[i];
}
cout << "Before Sorting: "; 
for (int i = 0; i < n; i++) {
cout << arr[i] << " "; cout << endl;
}
// Bubble Sort
for (int i = 0; i < n - 1; i++) {
for (int j = 0; j < n - i - 1; j++) {
 if (arr[j] > arr[j + 1]) {
int temp = arr[j]; 
arr[j] = arr[j + 1];
 arr[j + 1] = temp;
}
}
 
}
cout << "After Sorting: "; 
for (int i = 0; i < n; i++){
cout << arr[i] << " "; cout << endl;
}
cout << "Maximum: " << max << endl; cout << "Minimum: " << min << endl; 
return 0;
}
