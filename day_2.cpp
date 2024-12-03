#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>

int main(int argc, char** argv)
{
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    int answer = 0;
    std::string buf;
    bool non_decreasing;
    std::vector<int> report;
    int p1, p2, current, last;
    bool valid = true;

    fp = fopen("day_2.data", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        printf("Retrieved line of length %zu:\n", read);
        printf("%s", line);
        buf = "";

        report = {};

        for (int index = 0; index < read; index++) {
            if (line[index] == ' ' || line[index] == '\n') {
                report.push_back(std::stoi(buf));
                buf = "";
            } else {
                buf += line[index];
            }
        }

        p1 = 0;
        p2 = 1;

        if (report[1] >= report[0]) {
            non_decreasing = true;
        } else {
            non_decreasing = false;
        }

        valid = true;
        while (p2 < report.size() && valid == true) {
            current = report[p2];
            last = report[p1];
            if (non_decreasing == true) {
                if (current <= last or current > last + 3) {
                    valid = false;
                }
            } else {
                if (current >= last or current < last - 3) {
                    valid = false;
                }
            }

            p1++;
            p2++;
        }

        if (valid == true) {
            answer++;
        }
    }

    fclose(fp);
    if (line)
        free(line);

    std::cout << answer << std::endl;
    exit(EXIT_SUCCESS);
}
