// #include <iostream>
// #include <vector>
// using namespace std;

// int main(){

    // vector<char> vec={'a','b','c','d','e'};
    // vec.push_back('K'); 
    // cout<<"Size of Vector is:" <<vec.size() <<endl;
    // vec.pop_back();
    // cout<<"Size of Vector is:" <<vec.size() <<endl;
    // for(char val : vec){
    //     cout<<val<<endl;}
    // cout<<vec.front()<<endl;
    // cout<<vec.back()<<endl;
    // cout<<vec.at(2)<<endl;

    // vector<int> vec;
    // vec.push_back(0);
    // vec.push_back(1);
    // vec.push_back(2);
    // vec.push_back(3);
    // vec.push_back(4);

    // cout<<vec.size()<<endl;
    // cout<<vec.capacity()<<endl;

//     vector<int>&nums;
//     int ans=0;
//     for(int val:nums){
//         ans=ans^val;

//     }

//     return 0;
// }

// #include <iostream>
// #include <vector>
// #include <climits>
// using namespace std;

// int main(){

    // int n=5;
    // int arr[5]={1,2,3,4,5};

    // for(int st=0; st<n; st++){
    //     for(int end=st;end<n;end++){
    //         for(int i=st;i<=end;i++){
    //             cout<<arr[i];
    //         }
    //         cout<<" ";
    //     }
    //     cout<<endl;
    // }

//     int n=7;
//     int arr[7]={3,-4,5,4,-1,7,8};

//     int maxSum=INT_MIN;

//     for(int st=0;st<n;st++){
//         int currSum=0;
//         for(int end=st;end<n;end++){
//             currSum+=arr[end];
//             maxSum=max(currSum,maxSum);
//         }
//     }
//     cout<<"Max Subarray Sum= "<<maxSum<<endl;

//     return 0;
// }

// #include <iostream>
// #include <vector>
// #include <climits>
// using namespace std;

// int main(){
    
//     int n=7;
//     int arr[7]={3,-4,5,4,-1,7,-8};
    
//     int currSum=0;
//     int maxSum=INT_MIN;
//     for(int i=0;i<n;i++){
//         currSum+=arr[i];
//         maxSum=max(currSum,maxSum);
//         if(currSum<0){
//             currSum=0;
//         }
//     }
//     cout<<"The Maximum Sum of Sub Arrays is: "<<maxSum<<endl;
//     cout<<"The Value of Current Sum is: "<<currSum<<endl;
//     return 0;
// }
// #include <iostream>
// #include <vector>
// #include <climits>
// using namespace std;

// vector<int>pairSum(vector<int> nums,int target){
//     vector<int> ans;
//     int n=nums.size();

//     for(int i=0;i<n;i++){
//         for(int j=i+1;j<n;j++){
//             if(nums[i]+nums[j]==target){
//                 ans.push_back(i);
//                 ans.push_back(j);
//                 return ans;
//             }
//     }    
//     }
// }

// int main(){
    
//     vector<int>nums={1,3,2,7,11,15};
//     int target=9;

//     vector<int>ans=pairSum(nums,target);
//     cout<<ans[0]<<","<<ans[1]<<endl;
//     return 0;
// }

// #include <iostream>
// #include <vector>
// #include <climits>
// using namespace std;

// vector<int> pairSum(vector<int>nums, int target){
    
//     int n=nums.size();
//     vector<int>ans;
//     int i=0;int j=n-1;
    
//     while (i<j){
//         int Ps=nums[i]+nums[j];
//         if(Ps>target){
//             j--;
//         }else if(Ps<target){
//             i++;
//         }else{
//             ans.push_back(i);
//             ans.push_back(j);
//             return ans;
//         }
//     }
//     return {};
// }
// int main(){
    
//     vector<int>nums={2,7,11,15};
//     int target=15;
    
//     vector<int>ans=pairSum(nums,target);
//     if(ans.empty()){
//         cout<<"No Matching Pair Found from given.";
//     }else{
//         cout<<"Pair Found at index: "<< ans[0]
//         <<" and "<<ans[1]<<endl;
//     }
//     return 0;
// }

// #include <iostream>
// #include <vector>
// #include <climits>
// using namespace std;

// int main(){
//     int ans;
//     int n=5;
//     vector<int>nums={1,2,2,1,1};
//     for(int val:nums){
//         int freq=0;
//         for(int ele:nums){
//             if(ele==val){
//                 freq++;
//             }
//         }
//         if(freq>n/2){
//             ans=+val;
//         }
//     } 
//     cout<<ans<<endl;

//     return 0;
// }

// #include <iostream>
// #include <vector>
// #include <climits>
// using namespace std;
// class Solution {
// public:
//     int majorityElement(vector<int>& nums) {
//         int n=nums.size();

//         //sort
//         sort(nums.begin(),nums.end());

//         //freq count
//         int freq=1; int ans=nums[0];

//         for(int i=1;i<n;i++){
//             if(nums[i]==nums[i-1]){
//                 freq++;
//             }else{
//                 freq=1;
//                 ans=nums[i];
//             }
//             if(freq>n/2){
//                 return ans;
//             }
//         }
//         return ans;
//     }
// };
// int main(){



//     return 0;
// }

// #include <iostream>
// using namespace std;

// int main(){
//     /*
// VARIABLE: A variable is a named storage location used to store data.
// cin is used to take input from the user.
// cout is used to display output on the screen.
// */
//     string name;   
//     string department;   
//     int age;
//     float gpa;

//     cout<<"Enter Name:";     //COUT: It is used to display output on the screen.//
//     cin>>name;              //CIN: It is used to take input from the user.//
//     cout<<"Enter Age:";
//     cin>>age;
//     cout<<"Enter GPA:";
//     cin>>gpa;
//     cout<<"Enter Departemnt:";
//     cin>>department;

//     cout<<"Student:"<<name<<endl;
//     cout<<"AGE:"<<age<<endl;
//     cout<<"GPA:"<<gpa<<endl;
//     cout<<"Departemnt:"<<department<<endl;
//     cout<<"Birth Year:"<<2026-age<<endl;
//     return 0;
// }

#include <iostream>
using namespace std;

int main(){
    char grade;
    double fee;

    cout<<"Enter the grade:";
    cin>>grade;
    cout<<"Enter the fee:";
    cin>>fee;

    cout<<"Fee is:"<<fee<<endl;
    cout<<"Grade is:"<<grade<<endl;
    return 0;
}