#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LENGTH 51

int is_vps(char* string) {
    int length = strlen(string);
    int stack[MAX_LENGTH] = {0};
    int top = -1;
    
    for (int i = 0; i < length; i++) {
        if (string[i] == '(') {
            stack[++top] = 1;
        }
        else if (string[i] == ')') {
            if (top < 0) {
                return 0;
            }
            top--;
        }
    }
    
    return top == -1;
}

int main() {
    int t;
    scanf("%d", &t);
    char vps[MAX_LENGTH];
    
    for (int i = 0; i < t; i++) {
        scanf("%s", vps);
        if (is_vps(vps)) {
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }
    }
    
    return 0;
}
