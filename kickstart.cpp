// #include<bits/stdc++.h>
// using namespace std;

// void fun()
//     {
//       string s;
//       int n,fin=1;
//       cin>>n>>s;
//       for(int i =0;i<n;i++){
//         if( (int(s[i]))<int(s[i+1])){cout<<fin<<" ";fin++;}
//         else{cout<<fin<<" ";fin=1;}
//       }
//       cout<<endl;
//     }


// int main()
// {
//   int t;
//   cin>>t;
//   int i=0;
//   while(t--){
//     cout<<"Case #"<<i+1<<":"<<" ";
//     i++;
//     fun();}return 0;
// }






// // Time - O(N^3), Space - O(1)
// // Bruteforce solution
// int Solution::solve(const vector<int> &A) {
//     int n = A.size();
//     if(n <= 2) {
//         return n;
//     }
//     int max_len = 2;
//     for(int i = 0; i < n - 1; i++) {
//         for(int j = i + 1; j < n; j++) {
//             int diff = A[j] - A[i];
//             int cur_len = 2;
//             int last = A[j];
//             for(int k = j + 1; k < n; k++) {
//                 if(A[k] - last == diff) {
//                     cur_len++;
//                     last = A[k];
//                 }
//             }
//             max_len = max(cur_len, max_len);
//         }
//     }

//     return max_len;
// }



// // Time - O(N^3), Space - O(N^2)
// // DP solution
// int Solution::solve(const vector<int> &A) {
//     int n = A.size();
//     if(n <= 2) {
//         return n;
//     }

//     vector<vector<int>> dp(n, vector<int>(n, 2));
//     int max_len = 2;
//     for(int i = 0; i < n - 1; i++) {
//         for(int j = i + 1; j < n; j++) {
//             int need = 2 * A[i] - A[j];
//             int pos = -1;
//             for(int k = i - 1; k >= 0; k--) {
//                 if(A[k] == need) {
//                     pos = k;
//                     break;
//                 }
//             }

//             if(pos != -1) {
//                 dp[i][j] = max(dp[i][j], dp[pos][i] + 1);
//             }
//             max_len = max(dp[i][j], max_len);
//         }
//     }

//     return max_len;
// }



// // Time - O(N^2), Space - O(N^2)
// // DP with hashing solution
// int Solution::solve(const vector<int> &A) {
//     int n = A.size();
//     if(n <= 2) {
//         return n;
//     }

//     vector<vector<int>> dp(n, vector<int>(n, 2));
//     unordered_map<int, int> pos;
//     int max_len = 2;
//     for(int i = 0; i < n - 1; i++) {
//         for(int j = i + 1; j < n; j++) {
//             int need = 2 * A[i] - A[j];
//             if(pos.count(need)) {
//                 dp[i][j] = max(dp[i][j], dp[pos[need]][i] + 1);
//             }
//             max_len = max(dp[i][j], max_len);
//         }
//         pos[A[i]] = i;
//     }

//     return max_len;
// }





// #include <bits/stdc++.h>
// using namespace std;

// bool isPrime(int number)
// {
//     for (int i = 2; i <= sqrt(number); i++)
//     {
//         if (number % i == 0)
//         {
//             return false;
//         }
//     }
//     return true;
// }

// long long unsigned int getIndex(vector<long long unsigned int> v, long long unsigned int K)
// {
//     auto it = find(v.begin(), v.end(), K);

//     if (it != v.end())
//     {
//         int index = it - v.begin();
//         return index;
//     }
//     else
//     {
//         return -1;
//     }
// }

// int main()
// {
//     int T;
//     cin >> T;
//     int first = 0;
//     int second = 0;
//     vector<long long unsigned int> primes;
//     for (int idx = 1; idx < T + 1; idx++)
//     {
//         long long unsigned int Z;
//         cin >> Z;
//         long long unsigned int i = 0;
//         long long unsigned int res = 0;
//         while (true)
//         {
//             if (isPrime(i))
//             {
//                 if (primes.size() == 0 || i > primes[primes.size() - 1])
//                 {
//                     primes.push_back(i);
//                 }
//                 if (primes.size() > 1)
//                 {
//                     long long unsigned int index = getIndex(primes, i);
//                     if (i * primes[index - 1] > Z)
//                     {
//                         res = primes[index - 2] * primes[index - 1];
//                         break;
//                     }
//                 }
//             }
//             i++;
//         }
//         cout << "Case #" << idx << ": " << res << endl;
//     }
// }


