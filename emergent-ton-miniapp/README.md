# Emergent - TON Crowdfunding Telegram MiniApp

## Descripción
Plataforma de crowdfunding en blockchain TON para emprendedores, donadores y ballenas. Integra donaciones, votación DAO-like y recompensas en diamantes.

## Estructura del Proyecto
- **backend/**: FastAPI + MongoDB
- **frontend/**: Expo React Native (en desarrollo)
- **webapp/**: Versión web básica para Telegram MiniApp

## Instalación Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## MiniApp Web
Abre `webapp/index.html` en Telegram WebApp o hostea en un servidor.

## Dirección de Donaciones
`UQD-Hh6Bb_hn3k0zrizn_e32-5dWPThZnCDT0qhOtwMxTkHc`

## Próximos Pasos
- Implementar smart contracts en FunC/Tact para escrow y Jetton tokens.
- Despliegue completo en TON.
- Integración real de transacciones.

¡Listo para testing y lanzamiento!
