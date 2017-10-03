//
//  sh.c
//  
//
//  Created by Steven on 5/25/17.
//
//

#include <stdlib.h>
#include <stdio.h>

#include <unistd.h>
#include <fcntl.h>
#include <sys/time.h>
#include <sys/types.h>
#include <utime.h>
#include <string.h>
#include <termios.h>
#include <signal.h>


//Steven Demartini
// Systtems programing assignment ch8
static void parse( char* input, char* args[] );

int main (int argc, char* args[])
{
    signal(SIGINT, SIG_IGN);//set signal ignore control c
    pid_t weirdInt;
    int compVal;
    int exitVal = 0;
    char * acommand[256];
    char inputt[256];
    int val1,val2;
    
    while(exitVal != 1)
    {
        compVal = 1;
        
        printf("$ ");
        fgets(inputt, 256, stdin);//get the line
        parse(inputt, acommand); //pase it and store it in command
        compVal = strcmp(acommand[0], "exit");
        if(acommand[0] == NULL){}
        else{
            if(compVal == 0)
                exitVal = 1;
            compVal = strcmp(acommand[0], "cd");
            if(compVal == 0)
            {
                if(chdir(acommand[1]) == 0){}
                else
                    perror(acommand[1]);
        
            }
            else
            {
                weirdInt = fork();
                if(weirdInt == -1)
                    perror("");
                else if(weirdInt == 0)
                {
                    if(execvp(acommand[0], acommand)){}
                    else
                        perror("");
                }
                else
                    val1 = wait(&val2);
            }
        }
    }
    
}


static void parse( char* input, char* args[] )
{
    int i = 0;
    
    // fgets reads the \n, so overwrite it
    input[strlen(input)-1] = '\0';
    
    // get the first token
    args[i] = strtok( input, " " );
    
    // get the rest of them
    while( ( args[++i] = strtok(NULL, " ") ) );
}
