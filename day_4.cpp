#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include "utils.h"

int find_xmas(std::vector<std::vector<char>> &matrix, int i, int j){
    std::vector<std::vector<int>> offsets = {
        {0,1},
        {1,0},
        {0,-1},
        {-1,0},
        {-1,-1},
        {1,1},
        {1,-1},
        {-1,1},
    };
    int answer = 0;
    int i2,j2;
    char elem;

    for(auto offset:offsets){
        i2 = i;
        j2 = j;

        for(int step = 0; step < 4;step++){
            elem = matrix[i2][j2];

            if(step == 3 && elem == 'S'){
                answer+=1;
            } 
            else if (step == 0 and elem == 'X'){
                continue; 
            }
            else if (step == 1 and elem == 'M') {
                continue;
            }
            else if (step == 2 and elem == 'A') {
                continue;
            }
            else {
                break;
            }
            i2+=offset[0];
            j2+=offset[1];
        }
    }

    return answer;
}

int solve(std::vector<std::vector<char>> &matrix)
{
    int answer = 0;
    std::cout << "Size matrix : " << matrix.size() << " * " << matrix[0].size() << std::endl;

    for(int i = 0 ; i< matrix.size();i++){
        for(int j = 0; j<matrix[0].size();j++){
            answer+=find_xmas(matrix,i,j);
        }
    }    

    return answer;
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

    //for(auto line: matrix){
     //   print_vector(line);
    //}

    std::cout << solve(matrix) << std::endl;

    exit(EXIT_SUCCESS);
}
