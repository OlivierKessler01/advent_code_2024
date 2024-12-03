#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include "utils.h"

bool rec(std::vector<int>& report, int index, bool non_decreasing, int previous, bool jumped_already){
    if(index >= report.size()) {
        return true;
    }
    int current = report[index];

    if (previous == current){
        return false;
    }

    if (non_decreasing == true) {
        if (current < previous or current > previous + 3) {
            return false;
        }
    } else {
        if (current > previous or current < previous - 3) {
            return false;
        }
    }

    if (rec(report, index+1, non_decreasing, current, jumped_already) == true) {
        return true;
    }

    if(jumped_already == false) {
        if (rec(report, index+2, non_decreasing, current, true) == true) {
            return true;
        }
    }

    return false;
}

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
    int p1, p2, current, previous;
    int valid = 0;

    fp = fopen("day_2.data", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        printf("\n");
        printf("Retrieved line of length %zu:, line : %s", read, line);
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
        print_vector(report);

        if (
            rec(report, 1, (report[1]-report[0] > 0), report[0], false) == true ||
            rec(report, 2, (report[2]-report[0] > 0), report[0], true) == true ||
            rec(report, 2, (report[2]-report[1] > 0), report[1], true) == true
        ) {
            answer++;
        }
    }

    fclose(fp);
    if (line)
        free(line);

    std::cout << "answer is : " << answer << std::endl;
    exit(EXIT_SUCCESS);
}
