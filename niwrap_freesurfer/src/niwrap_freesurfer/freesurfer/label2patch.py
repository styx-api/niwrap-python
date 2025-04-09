# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LABEL2PATCH_METADATA = Metadata(
    id="1c4c1eb31d054d348645153cd56891912e1a70b1.boutiques",
    name="label2patch",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


Label2patchParameters = typing.TypedDict('Label2patchParameters', {
    "__STYX_TYPE__": typing.Literal["label2patch"],
    "subject_name": str,
    "hemisphere": str,
    "label_file": InputPathType,
    "output_patch": str,
    "dilate": typing.NotRequired[float | None],
    "erode": typing.NotRequired[float | None],
    "close": typing.NotRequired[float | None],
    "subjects_dir": typing.NotRequired[str | None],
    "surface_name": typing.NotRequired[str | None],
    "write_surface": bool,
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
        "label2patch": label2patch_cargs,
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
    }.get(t)


class Label2patchOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label2patch(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def label2patch_params(
    subject_name: str,
    hemisphere: str,
    label_file: InputPathType,
    output_patch: str,
    dilate: float | None = None,
    erode: float | None = None,
    close: float | None = None,
    subjects_dir: str | None = None,
    surface_name: str | None = None,
    write_surface: bool = False,
) -> Label2patchParameters:
    """
    Build parameters.
    
    Args:
        subject_name: Subject name.
        hemisphere: Hemisphere (e.g. lh or rh).
        label_file: Label file name.
        output_patch: Output patch file.
        dilate: Dilate the label n times before creating the patch.
        erode: Erode the label n times before creating the patch.
        close: Close the label n times before creating the patch.
        subjects_dir: Use path as the SUBJECTS_DIR instead of environment.
        surface_name: Use name as the surface (default 'inflated').
        write_surface: Write output to a surface file (not a patch). Use .stl\
            in filename to only write the mesh covered by the label, saving it in\
            FS format will save full surface.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "label2patch",
        "subject_name": subject_name,
        "hemisphere": hemisphere,
        "label_file": label_file,
        "output_patch": output_patch,
        "write_surface": write_surface,
    }
    if dilate is not None:
        params["dilate"] = dilate
    if erode is not None:
        params["erode"] = erode
    if close is not None:
        params["close"] = close
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if surface_name is not None:
        params["surface_name"] = surface_name
    return params


def label2patch_cargs(
    params: Label2patchParameters,
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
    cargs.append("label2patch")
    cargs.append(params.get("subject_name"))
    cargs.append(params.get("hemisphere"))
    cargs.append(execution.input_file(params.get("label_file")))
    cargs.append(params.get("output_patch"))
    if params.get("dilate") is not None:
        cargs.extend([
            "-dilate",
            str(params.get("dilate"))
        ])
    if params.get("erode") is not None:
        cargs.extend([
            "-erode",
            str(params.get("erode"))
        ])
    if params.get("close") is not None:
        cargs.extend([
            "-close",
            str(params.get("close"))
        ])
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "-sdir",
            params.get("subjects_dir")
        ])
    if params.get("surface_name") is not None:
        cargs.extend([
            "-surf",
            params.get("surface_name")
        ])
    if params.get("write_surface"):
        cargs.append("-writesurf")
    return cargs


def label2patch_outputs(
    params: Label2patchParameters,
    execution: Execution,
) -> Label2patchOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Label2patchOutputs(
        root=execution.output_file("."),
    )
    return ret


def label2patch_execute(
    params: Label2patchParameters,
    execution: Execution,
) -> Label2patchOutputs:
    """
    Utility to create patches from label files in Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Label2patchOutputs`).
    """
    params = execution.params(params)
    cargs = label2patch_cargs(params, execution)
    ret = label2patch_outputs(params, execution)
    execution.run(cargs)
    return ret


def label2patch(
    subject_name: str,
    hemisphere: str,
    label_file: InputPathType,
    output_patch: str,
    dilate: float | None = None,
    erode: float | None = None,
    close: float | None = None,
    subjects_dir: str | None = None,
    surface_name: str | None = None,
    write_surface: bool = False,
    runner: Runner | None = None,
) -> Label2patchOutputs:
    """
    Utility to create patches from label files in Freesurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_name: Subject name.
        hemisphere: Hemisphere (e.g. lh or rh).
        label_file: Label file name.
        output_patch: Output patch file.
        dilate: Dilate the label n times before creating the patch.
        erode: Erode the label n times before creating the patch.
        close: Close the label n times before creating the patch.
        subjects_dir: Use path as the SUBJECTS_DIR instead of environment.
        surface_name: Use name as the surface (default 'inflated').
        write_surface: Write output to a surface file (not a patch). Use .stl\
            in filename to only write the mesh covered by the label, saving it in\
            FS format will save full surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Label2patchOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL2PATCH_METADATA)
    params = label2patch_params(
        subject_name=subject_name,
        hemisphere=hemisphere,
        label_file=label_file,
        output_patch=output_patch,
        dilate=dilate,
        erode=erode,
        close=close,
        subjects_dir=subjects_dir,
        surface_name=surface_name,
        write_surface=write_surface,
    )
    return label2patch_execute(params, execution)


__all__ = [
    "LABEL2PATCH_METADATA",
    "Label2patchOutputs",
    "Label2patchParameters",
    "label2patch",
    "label2patch_params",
]
