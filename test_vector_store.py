from app.services.vector_store import build_vector_index

try:
    count = build_vector_index()

    print("SUCCESS: Vector index created!")
    print("Total indexed chunks:", count)

except Exception as error:
    print("Vector index creation failed:")
    print(type(error).__name__, str(error))