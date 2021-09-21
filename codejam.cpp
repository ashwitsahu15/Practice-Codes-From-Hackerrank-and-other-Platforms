// #include<bits/stdc++.h>
// using namespace std;
// typedef long long int ll;

// int main()
// {
//     ll t,n,q;
//     cin>>t>>n>>q;
//     while(t-- !=0){
//     vector<ll> a;
    
//     cout<<"1 2 3"<<endl;
    
//     ll size=3;
//     ll p;
//     cin>>p;
//     if(p==2){
//         a.push_back(1);
//         a.push_back(2);
//         a.push_back(3);
        
//     }
//     else if(p==3){
//         a.push_back(1);
//         a.push_back(3);
//         a.push_back(2);
//     }
//     else{
//         a.push_back(2);
//         a.push_back(1);
//         a.push_back(3);
//     }
//     for(ll i=4;i<=(n);i++){
//         ll u=0;
//         ll v=size-1;
//         while(u<v){
//             ll mid=u+((v-u)/2);
//             cout<<a[mid]<<" "<<a[mid+1]<<" "<<(i)<<endl;
//             cin>>p;
//             if(p==a[mid]){
//                 v=mid;
//             }
//             else if(p==a[mid+1]){
                
//                 u=mid+1;
//             }
//             else{
//                 a.insert(a.begin()+mid+1,i);
//                 size++;
//                 break;
//             }
//         }
//         if(size!=i){
//             if(u==0){
//                 a.insert(a.begin(),i);
//             }
//             else{
//                 a.push_back(i);
//             }
//             size++;
//         }
//     }
//     for(auto zzz: a){
//         cout<<zzz<<" ";
//     }
//     cout<<endl;
//     cin>>p;
//     if(p==-1){
//         break;
//     }
// }
// }


// #include<bits/stdc++.h>
// using namespace std;
// typedef long long int ll;

// int main()
// {
//     ll t1,n,q;
//     cin>>t1>>n>>q;
//     while(t1-- !=0){
//     vector<ll> a;
    
//     cout<<"1 2 3"<<endl;
    
//     ll size=3;
//     ll p;
//     cin>>p;
//     if(p==2){
//         a.push_back(1);
//         a.push_back(2);
//         a.push_back(3);
        
//     }
//     else if(p==3){
//         a.push_back(1);
//         a.push_back(3);
//         a.push_back(2);
//     }
//     else{
//         a.push_back(2);
//         a.push_back(1);
//         a.push_back(3);
//     }
//     for(ll i=4;i<=(n);i++){
//         ll u=0;
//         ll v=size-1;
//         while(u<v){
//             ll mid=u+((v-u)/2);
//             cout<<a[mid]<<" "<<a[mid+1]<<" "<<(i)<<endl;
//             cin>>p;
//             if(p==a[mid]){
//                 v=mid;
//             }
//             else if(p==a[mid+1]){
                
//                 u=mid+1;
//             }
//             else{
//                 a.insert(a.begin()+mid+1,i);
//                 size++;
//                 break;
//             }
//         }
//         if(size!=i){
//             if(u==0){
//                 a.insert(a.begin(),i);
//             }
//             else{
//                 a.push_back(i);
//             }
//             size++;
//         }
//     }
//     for(auto zzz: a){
//         cout<<zzz<<" ";
//     }
//     cout<<endl;
//     cin>>p;
//     if(p==-1){
//         break;
//     }
// }
// }



#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main(){
    
    int t;
    cin>>t;
    while(t--){
        ll n;
        ll x;
        cin>>n;
        vector<ll> v;
        for(int i=0;i<n;i++){
            cin>>x;
            v.push_back(x);
        }
        
        int count=0;
        int i=0;
        int current = v[i];
        for(int j=1;j<n;j++){
            if(current>v[j]-1){
                while(!(current< v[j])){
                    string n = to_string(v[j]);
                    string m ="9";
                    n.append(m);
                    v[j]=stoi(n);
                    count++;
                }
            }
                else{
                    i++;
                }
            }
            cout<<count<<endl;
        }
    return 0;
}