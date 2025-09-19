import joblib
import pandas as pd
from APP.Core.config import settings
from APP.cache.redis_cache import set_cached_pediction, get_cached_prediction

model = joblib.load(settings.MODEL_PATH)


def predict_car_price(data: dict):
    cache_key = " ".join([str(val) for val in data.values()])
    cached = get_cached_prediction(cache_key)
    if cached:
        return cached
    
    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]
    set_cached_pediction(cache_key, prediction)
    return prediction

