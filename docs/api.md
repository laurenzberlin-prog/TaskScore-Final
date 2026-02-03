# API – TaskScore

## GET /api/status

Gibt den aktuellen Status des Nutzers im JSON-Format zurück.

### Response (Beispiel)
```json
{
  "budget": 100,
  "current_total": 42,
  "done_points": 28,
  "done_score": 7,
  "task_count": 12
}