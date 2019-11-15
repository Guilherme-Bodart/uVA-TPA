package com.douglas.dynamicprogramming.uva10901;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/* Main.java
 * UVa 10901 - Ferry Loading III
 *
 * @author Douglas Bolis.
 */

public class Main {

    private final Scanner scanner = new Scanner(System.in);
    private final String LEFT = "left";
    private final String RIGHT = "right";

    public static void main(String[] args) {
        Main main = new Main();
        main.run();
    }

    public void run() {
        int numberCases = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < numberCases; i++) {
            String[] caseConfig = scanner.nextLine().split(" ");
            int maxCountCars = Integer.parseInt(caseConfig[0]);
            int crossingTime = Integer.parseInt(caseConfig[1]);
            int numberCars = Integer.parseInt(caseConfig[2]);

            FerryLoading ferry = new FerryLoading(maxCountCars, crossingTime, numberCars);

            ferry.solve();

            if (i + 1 < numberCases) {
                System.out.println("");
            }
        }
    }

    private class FerryLoading {

        private final Queue<int[]> right;
        private final Queue<int[]> left;
        private final int maxCountCars;
        private final int crossingTime;
        private final int numberCars;

        FerryLoading(int maxCountCars, int crossingTime, int numberCars) {
            this.right = new LinkedList<>();
            this.left = new LinkedList<>();
            this.maxCountCars = maxCountCars;
            this.crossingTime = crossingTime;
            this.numberCars = numberCars;
        }

        public void solve() {
            // Capturando os dados dos carros e armazenando-os nas filas.
            fillQueues();

            // Calculando os tempos de cruzamento para todos os carros.
            int[] crossingTotalTime = calcTime();

            for (int time : crossingTotalTime) {
                System.out.println(time);
            }
        }

        /**
         * Preenche as filas de embarque na margem esquerda e direita do rio.
         *
         */
        public void fillQueues() {
            for (int i = 0; i < numberCars; i++) {
                String[] bufferCar = scanner.nextLine().split(" ");
                int[] car = {i, Integer.parseInt(bufferCar[0])};

                if (bufferCar[1].equals(LEFT)) {
                    left.add(car);
                } else {
                    right.add(car);
                }
            }
        }

        /**
         * Calcula o tempo dos carros para cruzar o rio.
         *
         * @return Vetor com o tempo do cruzamento de todos os carros.
         */
        public int[] calcTime() {
            String currentBank = LEFT;
            Queue<int[]> auxQueue1, auxQueue2;

            int[] finalTimeCars = new int[numberCars];
            int time = 0;

            while (!left.isEmpty() || !right.isEmpty()) {
                int countEnqueuedCars = 0;

                // Definindo os sentidos dos carros para cruzar o rio.
                if (currentBank.equals(LEFT)) {
                    auxQueue1 = left;
                    auxQueue2 = right;
                } else {
                    auxQueue1 = right;
                    auxQueue2 = left;
                }

                // Embarcando os carros na balsa para cruzar o rio.
                while (countEnqueuedCars < maxCountCars && !auxQueue1.isEmpty() && auxQueue1.peek()[1] <= time) {
                    int[] car = auxQueue1.remove();
                    finalTimeCars[car[0]] = time + crossingTime;
                    ++countEnqueuedCars;
                }

                if (countEnqueuedCars != 0 || (!auxQueue2.isEmpty() && auxQueue2.peek()[1] <= time)) {
                    time += crossingTime;
                    currentBank = changeDirectionFerry(currentBank);
                } else
                if (auxQueue1.isEmpty() || (!auxQueue2.isEmpty() && auxQueue2.peek()[1] < auxQueue1.peek()[1])) {
                    time = auxQueue2.peek()[1] + crossingTime;
                    currentBank = changeDirectionFerry(currentBank);
                } else {
                    time = auxQueue1.peek()[1];
                }
            }

            return finalTimeCars;
        }

        /**
         * Muda o sentido que balsa percorre.
         *
         * @return Sentido oposto da balsa atualmente.
         */
        public String changeDirectionFerry(String current) {
            return current.equals(LEFT) ? RIGHT : LEFT;
        }
        
    }

}
