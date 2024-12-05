#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include "utils.h"

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

void find_xmas(std::vector<std::vector<char>> &matrix, int i, int j, int &answer){
    int i2,j2;
    char elem;

    for(auto offset:offsets){
        i2 = i;
        j2 = j;

        for(int step = 0; step < 4;step++){
            if ((i2 < 0 or i2 == matrix.size()) || (i2 < 0 or i2 == matrix[0].size())){
                break;
            }
            elem = matrix[i2][j2];

            if(step == 3 && elem == 'S'){
                answer+=1;
            } 
            else if ((step == 0 && elem != 'X') ||
                    (step == 1 && elem != 'M') ||
                    (step == 2 && elem != 'A')) 
            {
                break;
            }
            i2+=offset[0];
            j2+=offset[1];
        }
    }

    return;
}

void solve(std::vector<std::vector<char>> &matrix, int &answer)
{
    std::cout << "Size matrix : " << matrix.size() << " * " << matrix[0].size() << std::endl;

    for(int i = 0 ; i< matrix.size();i++){
        for(int j = 0; j<matrix[0].size();j++){
            find_xmas(matrix,i,j,answer);
        }
    }    

    return;
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
    solve(matrix,answer);
    std::cout << answer << std::endl;

    exit(EXIT_SUCCESS);
}
