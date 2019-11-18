import java.io.IOException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

/* Main.java
 * UVa 10172 - The Lonesome Cargo Distributor
 *
 * @authors Douglas Bolis.
 */

class Main {
    private final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        main.run();
    }

    public void run() {
        // Número de conjuntos de entrada no problema.
        int SET = scanner.nextInt();
        int N, S, Q;

        while(SET > 0) {
            // Número de estações.
            N = scanner.nextInt();
            // Capacidade do transportador de cargas.
            S = scanner.nextInt();
            // Número máximo de cargas que a fila na plataforma B pode acomodar.
            Q = scanner.nextInt();

            // Resolvendo o problema de distribição de carga.
            LonesomeCargoDistributor cargo = new LonesomeCargoDistributor(N, S, Q);
            cargo.solve();

            SET--;
        }
    }

    class LonesomeCargoDistributor {

        Map<Integer, Queue<Integer>> facility;
        int N, S, Q, qi;
        
        LonesomeCargoDistributor(int N, int S, int Q) {
            // Definindo a instalação para o transporte de cargas.
            facility = new HashMap<>();

            this.N = N;
            this.S = S;
            this.Q = Q;
        }

        public void solve() {
            for(int i = 1; i <= N; i++) {
                // Armazenando a capacidade de carga para cada estação.
                facility.put(i, new LinkedList());
                qi = scanner.nextInt();

                // Enfileirando as cargas na estação i.
                for(int j = 0; j < qi; j++) {
                    facility.get(i).add(scanner.nextInt());
                }
            }

            System.out.println(solveTotalMinutesJob());
        }

        public int solveTotalMinutesJob() {
            // Fila na plataforma B.
            Queue<Integer> platB;
            // Pilha da transportadora de cargas.
            Stack<Integer> carrier = new Stack<>();

            int minutes = 0;
            int i = 0;
            int cargo;

            while(!facilityIsEmpty() || !carrier.empty()) {
                i = (i % N) + 1;
                minutes += 2;
                platB = facility.get(i);

                // Enquanto a transportadora não estiver vazia e o topo da pilha cabe na plataforma A ou B.
                while(!carrier.empty() && (carrier.peek() == i || platB.size() < Q)) {
                    cargo = carrier.pop();
                    if (cargo != i) {
                        platB.add(cargo);
                    }
                    minutes++;
                }

                // Carrega transportadora enquanto a plataforma B possui cargas e a transportadora estiver vazia.
                while (platB.size() > 0 && carrier.size() < S) {
                    carrier.push(platB.poll());
                    minutes++;
                }
            }

            return ((minutes == 0) ? minutes : (minutes - 2));
        }

        public boolean facilityIsEmpty() {
            for(int i = 1; i <= N; i++) {
                if (facility.get(i).size() > 0) {
                    return false;
                }
            }
            return true;
        }
    }
}
