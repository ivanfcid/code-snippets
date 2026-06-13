#include <stdio.h>

int main(int argc, char **argv){
	if (argc > 1){
		FILE *file = fopen(argv[1], "r");
		if (file != NULL){
			char line [128];
			while(fgets(line, sizeof line, file) != NULL){
				printf("%s", line);
				/* fputs(line, stdout); */
			}
			fclose(file);
		}
		else perror(argv[1]); /* why didn't the file open? */
	}

	return 0;
   
}
