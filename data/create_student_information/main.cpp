#include <cstdio>
#include <cstring>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

const int limit_name_len = 8;
const int limit_class_id = 5;
int maxn = 1e3 + 5;

int main () {
    freopen ("/Users/chant/data/student_information.txt", "w", stdout);
    scanf ("%d", &maxn);
    srand(unsigned(time(NULL)));
    printf("%d\n", maxn);
    for (int i = 0; i < maxn; i++) {
        //INSERT INTO student_inf (identifier, major_id, name, class_id, enrollment_time) VALUES ("identifier", 4, "name", 4, "2020-09-27");
        std::string identifier = "student", name, enrollment_time;
        int major_id, class_id;
        int t = i;
        int res = 0;
        while (t) {
            res = res * 10 + t % 10;
            t /= 10;
        }
        while (res) {
            identifier += res % 10 + '0';
            res /= 10;
        }
        for (int j = 0; j < limit_name_len; j++) {
            name += rand()%26 + 'a';
        }
        enrollment_time = "2020-09-27";
        class_id = rand() % limit_class_id;
        major_id = limit_class_id - class_id;
        std::cout << identifier << std::endl << major_id << std::endl << name << std::endl << class_id << std::endl << enrollment_time << std::endl;
    }

    return 0;
}