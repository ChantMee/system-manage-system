#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

#define pii pair<std::string, int>
#define mp(a, b) make_pair(a, b)
#define fr first
#define sc second

const int maxn = 1e4 + 5;
const int limit_class_id = 5;
const int max_manage_major_num = 4;

std::pii res[maxn << 2];
int tot_res = 0;

std::string identifier[maxn];
std::string s;

int tot = 0;

// counselor_list
//#学生 老师 辅导员 门卫 管理员 超级管理员
//#0	 1		2     3   4     5
int main () {
    freopen ("/Users/chant/data/member_information_but_student.txt", "r", stdin);
    freopen ("/Users/chant/data/counselor_list_inf.txt", "w", stdout);
    int n, t;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> s >> t;
        if (t == 2) {
            identifier[tot++] = s;
        }
    }
    for (int i = 0; i < tot; i++) {
        int manage_major_num = rand() % limit_class_id;
        int vis[max_manage_major_num + 5];
        memset(vis, 0, sizeof vis);
        for (int j = 0; j < manage_major_num; j++) {
            int t = rand() % limit_class_id;
            while(vis[t]) {
                t = rand() % limit_class_id;
            }
            vis[t] = true;
            res[tot_res++] = std::mp(identifier[i], t);
        }
    }
    std::cout << tot_res << std::endl;
    for (int i = 0; i < tot_res; i++) {
        std::cout << res[i].fr << std::endl << res[i].sc << std::endl;
    }

    return 0;
}