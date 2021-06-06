#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <map>

#define pii pair<std::string, int>
#define mp(a, b) make_pair(a, b)
#define fr first
#define sc second

const int maxn = 1e3 + 5;
const int max_manage_class = 4;
const int limit_class_id = 5;

std::string identifier[maxn];
std::string s;
std::pii res[maxn << 2];
int tot = 0, tot_res = 0;

int main () {
    freopen ("/Users/chant/data/member_information_but_student.txt", "r", stdin);
    freopen ("/Users/chant/data/teacher_list_inf.txt", "w", stdout);
    srand((unsigned)time(NULL));
    int n, t;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> s >> t;
        if (t == 1) {
            identifier[tot++] = s;
        }
    }
    for (int i = 0; i < tot; i++) {
        int manage_class = rand() % max_manage_class;
        bool vis[maxn];
        memset(vis, 0, sizeof vis);
        for (int j = 0; j < manage_class; j++) {
            int t = rand() % limit_class_id;
            while (vis[t]) {
                t = rand() % limit_class_id;
            }
            vis[t] = true;
//            std::cout << identifier[i] << std::endl << t << std::endl;
            res[tot_res++] = std::mp(identifier[i], t);
        }
    }
    std::cout << tot_res << std::endl;
    for (int i = 0; i < tot_res; i++) {
        std::cout << res[i].fr << std::endl << res[i].sc << std::endl;
    }

    return 0;
}