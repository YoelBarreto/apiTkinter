from dataclasses import dataclass


@dataclass
class Meta:
    createdAt: str
    updatedAt: str
    barcode: int
    qrCode: str
