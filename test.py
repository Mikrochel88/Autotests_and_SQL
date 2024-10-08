# Артем Белоусов, 22-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_get_order_from_track():
    response_track = sender_stand_request.post_new_order(data.order_body)
    track = response_track.json()['track']
    response = sender_stand_request.get_order_from_track(track)
    assert response.status_code == 200