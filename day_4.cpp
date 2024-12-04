#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include "utils.h"

int solve(std::vector<std::vector<char>> matrix)
{
    return 10;
}

int main(int argc, char** argv)
{
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    int answer = 0;
    std::vector<char> report;
    std::vector<std::vector<char>> matrix;

    fp = fopen("day_4.data", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);
    
    while ((read = getline(&line, &len, fp)) != -1) {
        printf("Retrieved line of length %zu:\n", read);
        printf("%s", line);
        report = {};

        for (int index = 0; index < read -1 ; index++) {
            report.push_back(line[index]);
        }

        matrix.push_back(report);
    }

    fclose(fp);
    if (line)
        free(line);

    for(auto line: matrix){
        print_vector(line);
    }
    

    std::cout << solve(matrix) << std::endl;

    exit(EXIT_SUCCESS);
}
