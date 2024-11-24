public class Main {
    public static void main(String[] args) {
        // String (equivalent to Python's str)
        String x1 = "Hello World";
        System.out.println("String: " + x1);
        
        // Integer (equivalent to Python's int)
        int x2 = 20;
        System.out.println("int: " + x2);
        
        // Float (equivalent to Python's float)
        float x3 = 20.5f;  // 'f' is required to indicate float
        System.out.println("float: " + x3);
        
        // Double (equivalent to Python's complex, but only for real values)
        double x4 = 1.0;  // No direct complex type in Java
        System.out.println("double: " + x4);
        
        // Array (equivalent to Python's list)
        String[] x5 = {"apple", "banana", "cherry"};
        System.out.println("Array: ");
        for (String item : x5) {
            System.out.println(item);
        }
        
        // Tuple (not directly supported in Java, but we can use an Array or List for similar functionality)
        // Here, we'll use an Array for simplicity
        String[] x6 = {"apple", "banana", "cherry"};
        System.out.println("Tuple (using Array): ");
        for (String item : x6) {
            System.out.println(item);
        }
        
        // Range (not directly supported in Java, but we can simulate it with loops)
        System.out.println("Range: ");
        for (int i = 0; i < 6; i++) {
            System.out.println(i);
        }
        
        // Map (equivalent to Python's dict)
        java.util.Map<String, Integer> x7 = new java.util.HashMap<>();
        x7.put("name", 36);
        x7.put("age", 36);
        System.out.println("Map (equivalent to dictionary): " + x7);
        
        // Set (equivalent to Python's set)
        java.util.Set<String> x8 = new java.util.HashSet<>();
        x8.add("apple");
        x8.add("banana");
        x8.add("cherry");
        System.out.println("Set: " + x8);
        
        // Immutable Set (equivalent to Python's frozenset)
        java.util.Set<String> x9 = java.util.Set.of("apple", "banana", "cherry");
        System.out.println("Immutable Set (equivalent to frozenset): " + x9);
        
        // Boolean (equivalent to Python's bool)
        boolean x10 = true;
        System.out.println("Boolean: " + x10);
        
        // Byte Array (equivalent to Python's bytes)
        byte[] x11 = "Hello".getBytes();
        System.out.println("Bytes: " + new String(x11));
        
        // Byte Array (equivalent to Python's bytearray)
        byte[] x12 = new byte[5];
        System.out.println("Byte Array: " + new String(x12));
        
        // Memory View (Java does not have a direct equivalent, but ByteBuffer is somewhat similar)
        java.nio.ByteBuffer x13 = java.nio.ByteBuffer.allocate(5);
        System.out.println("MemoryView (ByteBuffer): " + x13);
        
        // Null (equivalent to Python's None)
        Object x14 = null;
        System.out.println("Null (None equivalent): " + x14);
    }
}
