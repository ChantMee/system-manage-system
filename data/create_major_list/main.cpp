#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

#define pii pair<int, int>
#define mp(a, b) make_pair(a, b)
#define fr first
#define sc second

const int maxn = 1e5 + 5;
const int limit_class_id = 5;

std::pii res[maxn << 2];
int tot_res = 0;

int main () {
    freopen ("/Users/chant/data/major_list_inf.txt", "w", stdout);
    for (int i = 0; i < limit_class_id; i++) {
        int learn_major_num = rand() % limit_class_id;
        bool vis[100];
        memset(vis, 0, sizeof vis);
        for (int j = 0; j < learn_major_num; j++) {
            int t = rand() % limit_class_id;
            while(vis[t]) {
                t = rand() % limit_class_id;
            }
            vis[t] = true;
            res[tot_res++] = std::mp(i, t);
        }
    }
    std::cout << tot_res << std::endl;
    for (int i = 0; i < tot_res; i++) {
        std::cout << res[i].fr << std::endl << res[i].sc << std::endl;
    }

    return 0;
}