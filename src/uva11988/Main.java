/*
	Jadson Pereira
	uva11988 - Broken Keyboard
*/



import java.io.IOException;
import java.util.LinkedList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        LinkedList<Character> list = new LinkedList();
        int flag;
        int iHome; 
        while(scan.hasNext()) {
            list.clear();
            flag = 0;
            iHome = 0;
            String line = scan.nextLine();
            for(int i=0;i<line.length();i++){
                switch (line.charAt(i)) {
                    case '[':
                        flag = 1;
                        iHome = 0;
                        break;
                    case ']':
                        flag = 0;
                        break;
                    default:
                        if(flag == 0){
                            list.add(line.charAt(i));
                            iHome = 0;
                        }else{
                            list.add(iHome,line.charAt(i));
                            iHome++;
                        }   
                        break;
                }
                       
            }
            StringBuilder s = new StringBuilder();
            list.forEach(c->{
                s.append(c);
            });
            System.out.println(s);
        }
    scan.close();    
    }
    
}

