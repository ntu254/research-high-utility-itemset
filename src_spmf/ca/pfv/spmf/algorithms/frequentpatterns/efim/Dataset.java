package ca.pfv.spmf.algorithms.frequentpatterns.efim;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;

import ca.pfv.spmf.datastructures.collections.list.ArrayListObject;
import ca.pfv.spmf.datastructures.collections.list.ListObject;
/* This file is copyright (c) 2012-2015 Souleymane Zida, Philippe Fournier-Viger, Alan Souza
* 
* This file is part of the SPMF DATA MINING SOFTWARE
* (http://www.philippe-fournier-viger.com/spmf).
* 
* SPMF is free software: you can redistribute it and/or modify it under the
* terms of the GNU General Public License as published by the Free Software
* Foundation, either version 3 of the License, or (at your option) any later
* version.
* SPMF is distributed in the hope that it will be useful, but WITHOUT ANY
* WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
* A PARTICULAR PURPOSE. See the GNU General Public License for more details.
* You should have received a copy of the GNU General Public License along with
* SPMF. If not, see <http://www.gnu.org/licenses/>.
*/
/**
 * This is the parser class for the dataset.
 * It has actions related to parse a txt based file to a Dataset class.
 *
 * @see AlgoEFIM
 */
public class Dataset {

	/** the list of transactions in this dataset */
	ListObject<Transaction> transactions;

	/** the largest item name */
	private int maxItem = 0;

	/**
	 * Constructor
	 * @param datasetPath the path of the file containing the dataset
	 * @param maximumTransactionCount the number of transaction to be read from the input file
	 * @throws IOException exception if error reading the file
	 */
    public Dataset(String datasetPath, int maximumTransactionCount) throws IOException {

    	// Initialize a list to store transactions in memory
        transactions = new ArrayListObject<Transaction>();
        
        // Create a buffered reader to read the input file
        BufferedReader br = new BufferedReader(new FileReader(datasetPath));
        String line;
        int i=0;
        // iterate over the lines to build the transaction
        while((line = br.readLine()) != null) { 
			// if the line is  a comment, is  empty or is  metadata
			if (line.isEmpty() == true || line.charAt(0) == '#' 
					|| line.charAt(0) == '%' || line.charAt(0) == '@') {
				continue;
			}
			i++;
			// read the transaction
			transactions.add(createTransaction(line));
			// if the number of transaction to be read is reached, we stop
        	if(i==maximumTransactionCount) {
        		break;
        	}
			
        }
        //****** Show the number of transactions in this dataset**************************//
        System.out.println("Transaction count :" +  transactions.size());
        br.close();
    }

    /**
     * Create a transaction object from a line from the input file
     * @param line a line from input file
     * @return a transaction
     */
    private Transaction createTransaction(String line) {
        int len = line.length();
        int colon1 = line.indexOf(':');
        int colon2 = line.indexOf(':', colon1 + 1);

        int transactionUtility = 0;
        for (int i = colon1 + 1; i < colon2; i++) {
            char c = line.charAt(i);
            if (c >= '0' && c <= '9') {
                transactionUtility = transactionUtility * 10 + (c - '0');
            }
        }

        int itemCount = 0;
        boolean inToken = false;
        for (int i = 0; i < colon1; i++) {
            char c = line.charAt(i);
            if (c != ' ') {
                if (!inToken) {
                    itemCount++;
                    inToken = true;
                }
            } else {
                inToken = false;
            }
        }

        int[] items = new int[itemCount];
        int[] utilities = new int[itemCount];

        int idx = 0;
        int currentVal = 0;
        inToken = false;
        for (int i = 0; i <= colon1; i++) {
            char c = (i == colon1) ? ' ' : line.charAt(i);
            if (c >= '0' && c <= '9') {
                currentVal = currentVal * 10 + (c - '0');
                inToken = true;
            } else if (inToken) {
                items[idx++] = currentVal;
                if (currentVal > maxItem) {
                    maxItem = currentVal;
                }
                currentVal = 0;
                inToken = false;
            }
        }

        idx = 0;
        currentVal = 0;
        inToken = false;
        for (int i = colon2 + 1; i <= len; i++) {
            char c = (i == len) ? ' ' : line.charAt(i);
            if (c >= '0' && c <= '9') {
                currentVal = currentVal * 10 + (c - '0');
                inToken = true;
            } else if (inToken) {
                utilities[idx++] = currentVal;
                currentVal = 0;
                inToken = false;
            }
        }

        return new Transaction(items, utilities, transactionUtility);
    }

    /**
     * Get the list of transactions in this database
     * @return the list of transactions
     */
    public ListObject<Transaction> getTransactions() {
        return transactions;
    }


    /**
     * Get the largest item  in this database.
     * @return the largest item
     */
    public int getMaxItem() {
        return maxItem;
    }

   /**
    * Get a string representation of this database
    * @return a string
    */
    public String toString() {
    	// Create a stringbuilder for storing the string
        StringBuilder datasetContent = new StringBuilder();

        // We will append each transaction to this string builder
        for(int i=0; i< transactions.size(); i++) {
        	Transaction transaction = transactions.get(i);
            datasetContent.append(transaction.toString());
            datasetContent.append("\n");
        }
        // Return the string
        return datasetContent.toString();
    }

}
