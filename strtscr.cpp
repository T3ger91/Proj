#include <iostream>
#include <SFML/Graphics.hpp> // подключаем библиотеку SFML для работы с графикой

using namespace std;

int main()
{
    
    sf::RenderWindow window(sf::VideoMode(800, 600), "Game");

    // загружаем фоновую картинку
    sf::Texture bgTexture;
    if (!bgTexture.loadFromFile("background.jpg")) {
       
        cerr << "Не удалось загрузить картинку!" << endl;
        return 1;
    }

   
    sf::Sprite bgSprite(bgTexture);

    // устанавливаем размеры спрайта в соответствии с размерами окна
    bgSprite.setScale(window.getSize().x / bgSprite.getLocalBounds().width,
                      window.getSize().y / bgSprite.getLocalBounds().height);

    sf::RectangleShape startButton(sf::Vector2f(200, 50));
    startButton.setFillColor(sf::Color::Green);
    startButton.setOutlineThickness(5);
    startButton.setOutlineColor(sf::Color::White);

    
    startButton.setPosition(window.getSize().x / 2 - startButton.getSize().x / 2,
                            window.getSize().y / 2 - startButton.getSize().y / 2);

    
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();

            
            if (event.type == sf::Event::MouseButtonPressed && event.mouseButton.button == sf::Mouse::Left) {
                sf::Vector2f mousePos = window.mapPixelToCoords(sf::Mouse::getPosition(window));
                if (startButton.getGlobalBounds().contains(mousePos))
                    cout << "Кнопка \"Старт\" была нажата!" << endl;
            }
        }

        
        window.clear();
        window.draw(bgSprite);
        window.draw(startButton);
        window.display();
    }

    return 0;
}
