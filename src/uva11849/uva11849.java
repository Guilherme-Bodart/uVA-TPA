import java.util.HashSet;
import java.util.Scanner;


/* 
	Jadson Pereira
	UVa 11849 - CD
 */


public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m= scan.nextInt();
        int acc =0;
        while(n!=0 && m != 0){
            //cria TreeSet
            TreeSet<Integer> tsCds = new TreeSet<Integer>();
            //Adiciona os cds do Jack na Árvore
            for(int i=0;i<n;i++){
                int cdsJack = scan.nextInt();
                tsCds.add(cdsJack);
            }
            //Adiciona os cds do Jill   
            for(int i=0;i<m;i++){
                int cdsJills = scan.nextInt();
                //Caso o CD esteja na estrutura, soma no acumulador
                //Caso não, adiciona na estrutura.
                if(tsCds.contains(cdsJills)){
                    acc++;
                }else{
                    tsCds.add(cdsJills);
                }
            }
            System.out.println(acc);
            acc =0;
            n = scan.nextInt();
            m= scan.nextInt();
        }
    }
}
