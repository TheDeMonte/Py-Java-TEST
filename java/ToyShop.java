import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.PriorityQueue;

class Toy {
    int id;
    String name;
    int frequency;

    public Toy(int id, String name, int frequency) {
        this.id = id;
        this.name = name;
        this.frequency = frequency;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getFrequency() {
        return frequency;
    }
}

public class ToyShop {

    public static void main(String[] args) {
        Toy toy1 = new Toy(1, "Мишка", 5);
        Toy toy2 = new Toy(2, "Кукла", 3);
        Toy toy3 = new Toy(3, "Машинка", 4);

        PriorityQueue<Toy> queue = new PriorityQueue<>((t1, t2) -> t2.getFrequency() - t1.getFrequency());

        queue.add(toy1);
        queue.add(toy2);
        queue.add(toy3);

        try (BufferedWriter writer = new BufferedWriter(new FileWriter("output.txt"))) {
            for (int i = 0; i < 10; i++) {
                Toy toy = queue.poll();
                if (toy != null) {
                    writer.write("ID: " + toy.getId() + ", Наименование: " + toy.getName() + ", Частота выпадения: " + toy.getFrequency() + "\n");
                } else {
                    writer.write("Больше нет игрушек\n");
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}