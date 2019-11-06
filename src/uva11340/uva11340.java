import java.util.Scanner;

/* Main.java
 * UVa 11340 - Newspaper
 *
 * @authors Douglas Bolis, Guilherme Bodart e Jadson Pereira.
 */
public class Main {
    public final static int SIZE_ASCII_TABLE = 128;

    public static void main(String[] args) {
        try {
            Scanner in = new Scanner(System.in);
            int[] tableCosts = new int[SIZE_ASCII_TABLE];

            // Capturando o número de testes a serem realizado.
            int numberTests = in.nextInt();

            // Realizando cada teste da entrada de dados.
            for (int n = 0; n < numberTests; n++) {
                // Capturando o número de caracteres que possuem custos.
                int numberCharacters = in.nextInt();
                int finalCost = 0;

                // Preenchendo o vetor com -1.
                for (int i = 0; i < SIZE_ASCII_TABLE; i++) {
                    tableCosts[i] = -1;
                }

                // Capturando e armazenando os caracteres com os seus custos na tabela de custos.
                for (int i = 0; i < numberCharacters; i++) {
                    int charKey = (int) in.next().charAt(0);
                    int charCost = in.nextInt();
                    tableCosts[charKey] = charCost;
                }

                // Capturando o número de linhas que o artigo contém.
                int numberLinesArticle = in.nextInt();
                in.nextLine();

                // Capturando o artigo e calculando o seu custo de acordo com a tabela de custos.
                for (int j = 0; j < numberLinesArticle; j++) {
                    String lineArticle = in.nextLine();
                    // Percorrendo cada caracter do artigo.
                    for (int k = 0; k < lineArticle.length(); k++) {
                        int charKey = (int) lineArticle.charAt(k);
                        // Verificando se o caracter possui um custo na tabela de custos.
                        finalCost += (charKey < 0 || charKey >= SIZE_ASCII_TABLE || tableCosts[charKey] < 0) ? 0 : tableCosts[charKey];
                    }
                }

                System.out.println(String.format((finalCost % 100 < 10) ? "%d.0%d$" : "%d.%d$", finalCost / 100, finalCost % 100));
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            System.exit(0);
        }
    }
}

