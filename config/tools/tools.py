from datetime import datetime, timedelta
from typing import Optional, List, Dict
from config.tools.switchers import *
from swarm.core import Result
import json


def check_date_availability(
    date: str, time_slot: Optional[str] = None
) -> Dict[str, bool]:
    """
    Check if a specific date and optional time slot is available

    Args:
        date: Date in YYYY-MM-DD format
        time_slot: Optional time slot in HH:MM format

    Returns:
        Dictionary with availability status
    """
    print(f"🔍 Verificando disponibilidad para fecha: {date}, horario: {time_slot}")
    # Mock implementation
    return {"is_available": True}


def get_available_slots(date: str) -> List[str]:
    """
    Get all available time slots for a specific date

    Args:
        date: Date in YYYY-MM-DD format

    Returns:
        List of available time slots in HH:MM format
    """
    print(f"📅 Buscando horarios disponibles para: {date}")
    # Mock implementation
    slots = ["09:00", "10:00", "11:00", "14:00", "15:00"]
    print(f"✅ Se encontraron {len(slots)} horarios disponibles")
    return slots


def get_calendar_info(start_date: str, end_date: str) -> Dict[str, List[str]]:
    """
    Get calendar availability for a date range

    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format

    Returns:
        Dictionary with dates and their available slots
    """
    print(f"📊 Consultando calendario desde {start_date} hasta {end_date}")
    # Mock implementation
    result = {"2024-03-20": ["09:00", "10:00"], "2024-03-21": ["14:00", "15:00"]}
    print(f"📋 Información del calendario recuperada para {len(result)} días")
    return result


def get_operating_hours() -> Dict[str, Dict[str, str]]:
    """
    Get business operating hours

    Returns:
        Dictionary with operating hours per day
    """
    print("⏰ Obteniendo horario de operación")
    # Mock implementation
    print("✨ Horario de operación recuperado exitosamente")
    return {
        "monday": {"open": "09:00", "close": "17:00"},
        "tuesday": {"open": "09:00", "close": "17:00"},
        "wednesday": {"open": "09:00", "close": "17:00"},
        "thursday": {"open": "09:00", "close": "17:00"},
        "friday": {"open": "09:00", "close": "16:00"},
    }


def book_visit(
    date: str,
    time_slot: str,
    num_people: int,
    contact_info: Dict[str, str],
    tour_city: str,
) -> Dict[str, any]:
    """
    Book a visit for a spot for a specific date and time

    Args:
        date: Date in YYYY-MM-DD format
        time_slot: Time slot in HH:MM format
        num_people: Number of people for the tour
        contact_info: Dictionary with contact information (name, email, phone)
    Returns:
        Dictionary with booking details including confirmation number
    """
    print(
        f"📝 Procesando reserva para {num_people} personas el {date} a las {time_slot}"
    )
    # Mock implementation
    booking_reference = (
        f"VISITS-{datetime.now().strftime('%Y%m%d')}-{hash(date + time_slot)}"[:12]
    )

    result = {
        "booking_reference": booking_reference,
        "status": "confirmed",
        "date": date,
        "time": time_slot,
        "num_people": num_people,
        "total_price": num_people * 50.00,  # Precio mock de 50.00 por persona
        "contact_info": contact_info,
    }

    print(f"✅ Reserva confirmada con referencia: {booking_reference}")
    return result


def update_global_context(context: Dict[str, any], new_context: Dict[str, any]):
    """
    Update the global context with the latest information

    Args:
        context_variables: Dictionary with the current context variables
        new_context: Dictionary with the new context information
    """
    construct_context = json.loads(context)
    parsed_new_context = json.loads(new_context)

    construct_context["general_context"] = {
        **construct_context.get("general_context", {}),
        **parsed_new_context,
    }

    print(construct_context)

    return Result(value="Done", context_variables=construct_context)


def get_spot_data(spot_id: int):
    """
    This function retrieves the data of a spot from the database

    Args:
        spot_id: The id of the spot to be retrieved
    """
    print(f"🔍 Buscando información del lugar con ID: {spot_id}")
    # Mock implementation
    spot_data = {
        "spot_id": spot_id,
        "name": "Sample Spot",
        "type": "Retail",
        "square_metters": 100,
        "price": 1500,
        "location": "123 Main St",
        "fire_system": "Yes",
        "security_system": "Yes",
        "availability": True,
    }
    print(f"✅ Información del lugar recuperada exitosamente")
    return spot_data
