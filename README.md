# BettRIVM


BettRIVM is a backend-only **betting system** built with Django and Django REST Framework. It allows admins to create betting games, set odds, process payments, and track user bets.

## Features
- **User authentication** (Admin & Client roles)  
- **JWT-based authentication**
- **Game management**
- **Betting system**
- **Transaction tracking**

## Installation
1. Clone repository
2. Create virtual enviorment
3. Install dependencies - requirements
4. Apply migrations
5. Create superuser
6. Run the server

## Endpoints
| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| POST | /api/register/ | Register new users |
| POST | /api/token/ | Obtain JWT token |
| POST | /api/games/ | Create a new game (Admin) |
| GET | /api/games/ | View available games |
| GET | /api/bets/ | View bets |

## Future improvements
- **Implement front-end
- **Implement real-time bet updates
- **Add deposit/withdrawal functinoality
