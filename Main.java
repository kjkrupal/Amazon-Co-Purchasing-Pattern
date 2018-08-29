import java.util.HashMap;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.TreeMap;
import java.util.Collections; 
import java.util.Comparator; import java.util.HashMap; import java.util.LinkedHashMap; import java.util.Map; import static java.util.stream.Collectors.*; import static java.util.Map.Entry.*;


public class Main {
    
    public static void main(String[] args) throws Exception{
        
        ReadFile read_file = new ReadFile();
        
        ArrayList < HashMap > return_set = read_file.read(args[0]);

        @SuppressWarnings("unchecked")
        HashMap < Integer, ArrayList > itemset = return_set.get(0);

        @SuppressWarnings("unchecked")
        HashMap < String, Integer > item_support_unsorted = return_set.get(1);
        
        Map<String, Integer> item_support = item_support_unsorted .entrySet() .stream() .sorted(comparingByValue()) .collect( toMap(e -> e.getKey(), e -> e.getValue(), (e1, e2) -> e2, LinkedHashMap::new));
        
        item_support = item_support_unsorted .entrySet() .stream() .sorted(Collections.reverseOrder(Map.Entry.comparingByValue())) .collect( toMap(Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e2, LinkedHashMap::new));
        

    }

}


