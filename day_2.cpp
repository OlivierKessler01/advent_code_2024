
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdlib>
#include <iostream>


int main(int argc, char **argv) {
    
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;
    int answer = 0;
    std::string buf; 
    int last;
    int current;
    int non_decreasing;

    fp = fopen("day_2.data", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        printf("Retrieved line of length %zu:\n", read);
        printf("%s", line);
        last = -1;
        current = -1;
        non_decreasing = 0;
        
        for(int index = 0; index < read;index++){
            if (line[index] == ' '){
                current = std::stoi(buf);
                if (last > -1){
                    
                }
                last = current;
            } else {
                buf+=line[index];
            }
        }


    }

    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);   
    



    std::cout << answer << std::endl;
}
