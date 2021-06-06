#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

const int maxn = 1e3 + 5;
const int num_request = 500;
const int len_leave_reason = 50;

std::string identifier[maxn];
int tot = 0;
std::string s;

int main () {
    freopen ("/Users/chant/data/student_information.txt", "r", stdin);
    freopen ("/Users/chant/data/request_information.txt", "w", stdout);
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> s;
        identifier[tot++] = s;
        std::cin >> s >> s >> s >> s;
    }

    //identifier, leave_type, time_start, time_end, leave_reason
    std::cout << num_request << std::endl;
    srand((unsigned)time(NULL));
    for (int i = 0; i < num_request; i++) {
        int cur = rand() % tot;
        int leave_type = rand() & 1;
        std::string time_start = "2019-09-27 11:11:11";
        std::string time_end = "2020-09-27 11-11-11";
        std::string leave_reason = "xiang chi han bao wang, bu shi tai ju";
        std::cout << identifier[cur] << std::endl << leave_type << std::endl
            << time_start << std::endl << time_end << std::endl << leave_reason << std::endl;
    }

    return 0;
}