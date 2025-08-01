# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FSDCMDECOMPRESS_METADATA = Metadata(
    id="30d6a93931c489cde2efd8a6696b27e23a3c1869.boutiques",
    name="fsdcmdecompress",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


FsdcmdecompressParameters = typing.TypedDict('FsdcmdecompressParameters', {
    "__STYXTYPE__": typing.Literal["fsdcmdecompress"],
    "indcmfile": InputPathType,
    "outdcmfile": str,
    "dcmtk": bool,
    "jpeg": bool,
    "rle": bool,
    "gdcm": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "fsdcmdecompress": fsdcmdecompress_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "fsdcmdecompress": fsdcmdecompress_outputs,
    }.get(t)


class FsdcmdecompressOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsdcmdecompress(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """The decompressed DICOM file"""


def fsdcmdecompress_params(
    indcmfile: InputPathType,
    outdcmfile: str,
    dcmtk: bool = False,
    jpeg: bool = False,
    rle: bool = False,
    gdcm: bool = False,
) -> FsdcmdecompressParameters:
    """
    Build parameters.
    
    Args:
        indcmfile: Input DICOM file to decompress.
        outdcmfile: Output decompressed DICOM file.
        dcmtk: Use DCMTK for decompression (either dcmdrle.fs or dcmdjpeg.fs).
        jpeg: DICOM is JPEG compressed (ignored without --dcmtk).
        rle: DICOM is RLE compressed (ignored without --dcmtk).
        gdcm: Use GDCM for decompression (default).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fsdcmdecompress",
        "indcmfile": indcmfile,
        "outdcmfile": outdcmfile,
        "dcmtk": dcmtk,
        "jpeg": jpeg,
        "rle": rle,
        "gdcm": gdcm,
    }
    return params


def fsdcmdecompress_cargs(
    params: FsdcmdecompressParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("fsdcmdecompress")
    cargs.extend([
        "--i",
        execution.input_file(params.get("indcmfile"))
    ])
    cargs.extend([
        "--o",
        params.get("outdcmfile")
    ])
    if params.get("dcmtk"):
        cargs.append("--dcmtk")
    if params.get("jpeg"):
        cargs.append("--jpeg")
    if params.get("rle"):
        cargs.append("--rle")
    if params.get("gdcm"):
        cargs.append("--gdcm")
    return cargs


def fsdcmdecompress_outputs(
    params: FsdcmdecompressParameters,
    execution: Execution,
) -> FsdcmdecompressOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FsdcmdecompressOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(params.get("outdcmfile")),
    )
    return ret


def fsdcmdecompress_execute(
    params: FsdcmdecompressParameters,
    execution: Execution,
) -> FsdcmdecompressOutputs:
    """
    A tool for decompressing DICOM files using GDCM or DCMTK.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FsdcmdecompressOutputs`).
    """
    params = execution.params(params)
    cargs = fsdcmdecompress_cargs(params, execution)
    ret = fsdcmdecompress_outputs(params, execution)
    execution.run(cargs)
    return ret


def fsdcmdecompress(
    indcmfile: InputPathType,
    outdcmfile: str,
    dcmtk: bool = False,
    jpeg: bool = False,
    rle: bool = False,
    gdcm: bool = False,
    runner: Runner | None = None,
) -> FsdcmdecompressOutputs:
    """
    A tool for decompressing DICOM files using GDCM or DCMTK.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        indcmfile: Input DICOM file to decompress.
        outdcmfile: Output decompressed DICOM file.
        dcmtk: Use DCMTK for decompression (either dcmdrle.fs or dcmdjpeg.fs).
        jpeg: DICOM is JPEG compressed (ignored without --dcmtk).
        rle: DICOM is RLE compressed (ignored without --dcmtk).
        gdcm: Use GDCM for decompression (default).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FsdcmdecompressOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSDCMDECOMPRESS_METADATA)
    params = fsdcmdecompress_params(
        indcmfile=indcmfile,
        outdcmfile=outdcmfile,
        dcmtk=dcmtk,
        jpeg=jpeg,
        rle=rle,
        gdcm=gdcm,
    )
    return fsdcmdecompress_execute(params, execution)


__all__ = [
    "FSDCMDECOMPRESS_METADATA",
    "FsdcmdecompressOutputs",
    "FsdcmdecompressParameters",
    "fsdcmdecompress",
    "fsdcmdecompress_params",
]
