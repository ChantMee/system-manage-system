#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <ctime>
#include <iostream>

const int maxn = 3e2 + 5;
const int limit_class_id = 5;
//#学生 老师 辅导员 门卫 管理员 超级管理员
//#0	 1		2     3   4     5
const std::string identity_name[] = {"student", "teacher", "counselor", "guard", "admin", "super_admin"};
const bool ban_create_super_admin = true;
// major_id = limit_class_id - class_id

int cnt[6] = {0};


int main () {
    freopen ("/Users/chant/data/member_information_but_student.txt", "w", stdout);
    std::cout << maxn << std::endl;
    for (int i = 0; i < maxn; i++) {
        int identity = rand() % 5;
        std::string identifier = identity_name[identity];
        int t = cnt[identity]++;
        int cur = 0;
        while (t) {
            cur = cur * 10 + t % 10;
            t /= 10;
        }
        while(cur) {
            identifier += cur % 10 + '0';
            cur /= 10;
        }
        std::cout << identifier << std::endl << identity << std::endl;
    }

    return 0;
}