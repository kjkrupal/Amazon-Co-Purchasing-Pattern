import java.util.Scanner;
import java.util.HashMap;
import java.util.ArrayList;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

public class ReadFile {

    public ArrayList <HashMap> read(String file_name) throws FileNotFoundException {

        Scanner scanner = new Scanner(new File(file_name));

        HashMap < Integer, ArrayList > itemset = new HashMap < Integer, ArrayList > ();

        HashMap < String, Integer > item_support = new HashMap < String, Integer > ();

        ArrayList < HashMap > return_set = new ArrayList <HashMap> ();
        
        while (scanner.hasNext()) {
            String line = scanner.nextLine().toString();
            String[] values = line.split(",");
            ArrayList < String > basket = new ArrayList < String > ();
            for (int i = 1; i < values.length; i++) {
                basket.add(values[i]);
                int value;
                try {
                    value = item_support.get(values[i]);
                    value = value + 1;
                    item_support.put(values[i], value);
                } catch (NullPointerException e) {
                    item_support.put(values[i], 1);
                }
                
            }
            int key = Integer.parseInt(values[0]);
            itemset.put(key, basket);
        }

        scanner.close();
        return_set.add(itemset);
        return_set.add(item_support);
        return return_set;
    }

}