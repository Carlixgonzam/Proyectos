//Basic Poin

//Directiva
#include <stdio.h> //Preprocesador: Que incluye en el programa estandar de entrada y salida
//Manda llamar la biblioteca de las directivas
/*Funcion main inicia la ejecucion del programa*/

/*fin de  la funcion main*/


/*Funciones de suma*/
int main (){
    int num1;
    int num2;
    int resultado;
    printf("Ingrese el primer valor\n");
    scanf("%d", &num1);
    printf("Ingrese el segundo valor\n");
    scanf("%d", &num2);
    resultado = num1 + num2;
    printf("El resultado de la suma es:%d\n", resultado);
    return 0;
}
