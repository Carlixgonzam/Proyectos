import java.util.ArrayList;
import java.util.Scanner;

class Libro {
    private final String titulo;
    private final String autor;
    private final int anio;

    public Libro(String titulo, String autor, int anio) {
        this.titulo = titulo;
        this.autor = autor;
        this.anio = anio;
    }

    public String getTitulo() {
        return titulo;
    }
    public String getAutor() {
        return autor;
    }
    public int getAnio() {
        return anio;
    }
    @Override
    public String toString() {
        return "Título: " + titulo + ", Autor: " + autor + ", Año: " + anio;
    }
}

public class BibliotecaVirtual {
    private static ArrayList<Libro> biblioteca = new ArrayList<>();

    public static void agregarLibro() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el título del libro: ");
        String titulo = scanner.nextLine();

        System.out.print("Ingrese el autor del libro: ");
        String autor = scanner.nextLine();

        System.out.print("Ingrese el año de publicación: ");
        int anio = scanner.nextInt();

        Libro libro = new Libro(titulo, autor, anio);
        biblioteca.add(libro);

        System.out.println("¡Libro agregado con éxito!");
    }

    public static void buscarLibro() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el título del libro a buscar: ");
        String titulo = scanner.nextLine();

        boolean encontrado = false;
        for (Libro libro : biblioteca) {
            if (libro.getTitulo().equalsIgnoreCase(titulo)) {
                System.out.println("Libro encontrado: " + libro);
                encontrado = true;
                break;
            }
        }

        if (!encontrado) {
            System.out.println("Libro no encontrado.");
        }
    }

    public static void mostrarLibros() {
        if (biblioteca.isEmpty()) {
            System.out.println("La biblioteca está vacía.");
        } else {
            System.out.println("Libros en la biblioteca:");
            for (Libro libro : biblioteca) {
                System.out.println(libro);
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n--- Biblioteca Virtual ---");
            System.out.println("1. Agregar libro");
            System.out.println("2. Buscar libro");
            System.out.println("3. Mostrar libros");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");

            opcion = scanner.nextInt();
            scanner.nextLine(); // Limpiar buffer

            switch (opcion) {
                case 1:
                    agregarLibro();
                    break;
                case 2:
                    buscarLibro();
                    break;
                case 3:
                    mostrarLibros();
                    break;
                case 4:
                    System.out.println("Saliendo del programa...");
                    break;
                default:
                    System.out.println("Opción no válida.");
            }
        } while (opcion != 4);
    }
}

//Interfas grafica

package bibliotecavirtual:
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class BibliotecaVirtualGUI extends JFrame {
    private JPanel panel;
    private JButton agregarLibroButton;
    private JButton buscarLibroButton;
    private JButton mostrarLibrosButton;

    public BibliotecaVirtualGUI() {
        setTitle("Biblioteca Virtual");
        setContentPane(panel);
        pack();
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        agregarLibroButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(null, "Agregar libro");
            }
        });

        buscarLibroButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(null, "Buscar libro");
            }
        });

        mostrarLibrosButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(null, "Mostrar libros");
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new BibliotecaVirtualGUI();
        frame.setVisible(true);
    }
}

//Interfas grafica con eventos

package bibliotecavirtual;
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class BibliotecaVirtualGUI extends JFrame {
    private JPanel panel;
    private JButton agregarLibroButton;
    private JButton buscarLibroButton;
    private JButton mostrarLibrosButton;

    public BibliotecaVirtualGUI() {
        setTitle("Biblioteca Virtual");
        setContentPane(panel);
        pack();
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        agregarLibroButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String titulo = JOptionPane.showInputDialog("Ingrese el título del libro:");
                String autor = JOptionPane.showInputDialog("Ingrese el autor del libro:");
                int anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año de publicación:"));

                JOptionPane.showMessageDialog(null, "Libro agregado con éxito.");
            }
        });

        buscarLibroButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String titulo = JOptionPane.showInputDialog("Ingrese el título del libro a buscar:");

                JOptionPane.showMessageDialog(null, "Libro encontrado.");
            }
        });

        mostrarLibrosButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JOptionPane.showMessageDialog(null, "Mostrar libros");
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new BibliotecaVirtualGUI();
        frame.setVisible(true);
    }
}

//Interfas grafica con eventos y metodos

package bibliotecavirtual;
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class BibliotecaVirtualGUI extends JFrame {
    private JPanel panel;
    private JButton agregarLibroButton;
    private JButton buscarLibroButton;
    private JButton mostrarLibrosButton;

    public BibliotecaVirtualGUI() {
        setTitle("Biblioteca Virtual");
        setContentPane(panel);
        pack();
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        agregarLibroButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                agregarLibro();
            }
        });

        buscarLibroButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                buscarLibro();
            }
        });

        mostrarLibrosButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                mostrarLibros();
            }
        });
    }
}

