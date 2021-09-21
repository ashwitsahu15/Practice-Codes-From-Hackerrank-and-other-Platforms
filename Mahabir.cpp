#include<bits/stdc++.h>
using namespace std;
#define int long long

int solve1(int n) {
    if(n<4) return n;
    int x=0,i;
    for(i=1;x<n;i++) x+=i;
    return i-1;
}

int solve2(int n) {
    if(n<4) return n;
    int x=0,i=1;
    while (x<n) {
        x= i*(i-1) + i;
        i++;
    }
    return 2*i-3;
}

signed main() {
    int TT=1;
    cin>>TT;
    for(int tt=1;tt<=TT;tt++) {
        int n; cin>>n;
        int ans=solve1(n/2+n%2) + solve1(n/2);
        ans= min(ans, solve2(n));
        cout<<ans<<"\n";
    }
    return 0;
}