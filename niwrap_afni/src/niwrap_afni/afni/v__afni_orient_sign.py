# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__AFNI_ORIENT_SIGN_METADATA = Metadata(
    id="0406b1e6aa362529e558b94d8db55d746378a55d.boutiques",
    name="@AfniOrientSign",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VAfniOrientSignParameters = typing.TypedDict('VAfniOrientSignParameters', {
    "__STYXTYPE__": typing.Literal["@AfniOrientSign"],
    "infile": InputPathType,
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
        "@AfniOrientSign": v__afni_orient_sign_cargs,
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
        "@AfniOrientSign": v__afni_orient_sign_outputs,
    }.get(t)


class VAfniOrientSignOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__afni_orient_sign(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Output file containing the orientation signs of the dataset"""


def v__afni_orient_sign_params(
    infile: InputPathType,
) -> VAfniOrientSignParameters:
    """
    Build parameters.
    
    Args:
        infile: Input image file to determine orientation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@AfniOrientSign",
        "infile": infile,
    }
    return params


def v__afni_orient_sign_cargs(
    params: VAfniOrientSignParameters,
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
    cargs.append("@AfniOrientSign")
    cargs.extend([
        "-orient",
        execution.input_file(params.get("infile"))
    ])
    return cargs


def v__afni_orient_sign_outputs(
    params: VAfniOrientSignParameters,
    execution: Execution,
) -> VAfniOrientSignOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VAfniOrientSignOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(pathlib.Path(params.get("infile")).name + "_orient.txt"),
    )
    return ret


def v__afni_orient_sign_execute(
    params: VAfniOrientSignParameters,
    execution: Execution,
) -> VAfniOrientSignOutputs:
    """
    A tool within the AFNI suite to determine the orientation signs of datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VAfniOrientSignOutputs`).
    """
    params = execution.params(params)
    cargs = v__afni_orient_sign_cargs(params, execution)
    ret = v__afni_orient_sign_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__afni_orient_sign(
    infile: InputPathType,
    runner: Runner | None = None,
) -> VAfniOrientSignOutputs:
    """
    A tool within the AFNI suite to determine the orientation signs of datasets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile: Input image file to determine orientation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAfniOrientSignOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__AFNI_ORIENT_SIGN_METADATA)
    params = v__afni_orient_sign_params(
        infile=infile,
    )
    return v__afni_orient_sign_execute(params, execution)


__all__ = [
    "VAfniOrientSignOutputs",
    "VAfniOrientSignParameters",
    "V__AFNI_ORIENT_SIGN_METADATA",
    "v__afni_orient_sign",
    "v__afni_orient_sign_params",
]
