        double apprE = 0;
        int facTermCount = factorial(termCount);
        for (int i = termCount; i > 0; i--){
            apprE += 1/(facTermCount/i);
        }
        return apprE;