# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__XYZ_TO_IJK_METADATA = Metadata(
    id="c2f8c6ad40a232de3a6ff1e49118e8e23fa42606.boutiques",
    name="@xyz_to_ijk",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VXyzToIjkParameters = typing.TypedDict('VXyzToIjkParameters', {
    "__STYXTYPE__": typing.Literal["@xyz_to_ijk"],
    "inset": InputPathType,
    "x_coord": float,
    "y_coord": float,
    "z_coord": float,
    "prefix": typing.NotRequired[str | None],
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
        "@xyz_to_ijk": v__xyz_to_ijk_cargs,
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
        "@xyz_to_ijk": v__xyz_to_ijk_outputs,
    }.get(t)


class VXyzToIjkOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__xyz_to_ijk(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Output file containing the translated indices"""


def v__xyz_to_ijk_params(
    inset: InputPathType,
    x_coord: float,
    y_coord: float,
    z_coord: float,
    prefix: str | None = None,
) -> VXyzToIjkParameters:
    """
    Build parameters.
    
    Args:
        inset: Volumetric file name (e.g. FILE.nii.gz).
        x_coord: Three coordinates (in units of the dataset, like mm).
        y_coord: Three coordinates (in units of the dataset, like mm).
        z_coord: Three coordinates (in units of the dataset, like mm).
        prefix: File name (including path) to output the three indices.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@xyz_to_ijk",
        "inset": inset,
        "x_coord": x_coord,
        "y_coord": y_coord,
        "z_coord": z_coord,
    }
    if prefix is not None:
        params["prefix"] = prefix
    return params


def v__xyz_to_ijk_cargs(
    params: VXyzToIjkParameters,
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
    cargs.append("@xyz_to_ijk")
    cargs.extend([
        "-inset",
        execution.input_file(params.get("inset"))
    ])
    cargs.extend([
        "-xyz",
        str(params.get("x_coord"))
    ])
    cargs.append(str(params.get("y_coord")))
    cargs.append(str(params.get("z_coord")))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    return cargs


def v__xyz_to_ijk_outputs(
    params: VXyzToIjkParameters,
    execution: Execution,
) -> VXyzToIjkOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VXyzToIjkOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix")) if (params.get("prefix") is not None) else None,
    )
    return ret


def v__xyz_to_ijk_execute(
    params: VXyzToIjkParameters,
    execution: Execution,
) -> VXyzToIjkOutputs:
    """
    Helper script to convert (x, y, z) coordinates to (i, j, k) indices for a
    volumetric dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VXyzToIjkOutputs`).
    """
    params = execution.params(params)
    cargs = v__xyz_to_ijk_cargs(params, execution)
    ret = v__xyz_to_ijk_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__xyz_to_ijk(
    inset: InputPathType,
    x_coord: float,
    y_coord: float,
    z_coord: float,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> VXyzToIjkOutputs:
    """
    Helper script to convert (x, y, z) coordinates to (i, j, k) indices for a
    volumetric dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        inset: Volumetric file name (e.g. FILE.nii.gz).
        x_coord: Three coordinates (in units of the dataset, like mm).
        y_coord: Three coordinates (in units of the dataset, like mm).
        z_coord: Three coordinates (in units of the dataset, like mm).
        prefix: File name (including path) to output the three indices.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VXyzToIjkOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__XYZ_TO_IJK_METADATA)
    params = v__xyz_to_ijk_params(
        inset=inset,
        x_coord=x_coord,
        y_coord=y_coord,
        z_coord=z_coord,
        prefix=prefix,
    )
    return v__xyz_to_ijk_execute(params, execution)


__all__ = [
    "VXyzToIjkOutputs",
    "VXyzToIjkParameters",
    "V__XYZ_TO_IJK_METADATA",
    "v__xyz_to_ijk",
    "v__xyz_to_ijk_params",
]
