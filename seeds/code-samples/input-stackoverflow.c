#include<stdio.h>
#include<string.h>

void vulnerable_func(char *input) {
    char buf[100];
    strcpy(buf, input);
    printf("Received: %s\n", buf);
}

int main() {
    char input[200];
    printf("Enter input: ");
    gets(input);
    vulnerable_func(input);
    return 0;
}