# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DRIVE_SUMA_METADATA = Metadata(
    id="a84ac5b5fa5efa62f31e31f6fea077bf00c5e358.boutiques",
    name="DriveSuma",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


DriveSumaParameters = typing.TypedDict('DriveSumaParameters', {
    "__STYXTYPE__": typing.Literal["DriveSuma"],
    "command": str,
    "surf_label": typing.NotRequired[str | None],
    "surface_file": typing.NotRequired[InputPathType | None],
    "surf_state": typing.NotRequired[str | None],
    "surf_winding": typing.NotRequired[str | None],
    "coordinates": typing.NotRequired[InputPathType | None],
    "autorecord": typing.NotRequired[str | None],
    "background_color": typing.NotRequired[str | None],
    "view_file": typing.NotRequired[InputPathType | None],
    "do_file": typing.NotRequired[InputPathType | None],
    "do_draw_mask": typing.NotRequired[str | None],
    "fixed_do": typing.NotRequired[str | None],
    "mobile_do": typing.NotRequired[str | None],
    "key_press": typing.NotRequired[str | None],
    "viewer": typing.NotRequired[str | None],
    "anim_dup": typing.NotRequired[float | None],
    "save_as": typing.NotRequired[str | None],
    "save_index": typing.NotRequired[float | None],
    "save_range": typing.NotRequired[str | None],
    "save_last": bool,
    "save_last_n": typing.NotRequired[float | None],
    "save_all": bool,
    "echo_edu": bool,
    "echo_nel_stdout": bool,
    "echo_nel_stderr": bool,
    "examples": bool,
    "help": bool,
    "h": bool,
    "help_nido": bool,
    "c_demo": bool,
    "viewer_cont": bool,
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
        "DriveSuma": drive_suma_cargs,
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


class DriveSumaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `drive_suma(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def drive_suma_params(
    command: str,
    surf_label: str | None = None,
    surface_file: InputPathType | None = None,
    surf_state: str | None = None,
    surf_winding: str | None = None,
    coordinates: InputPathType | None = None,
    autorecord: str | None = None,
    background_color: str | None = None,
    view_file: InputPathType | None = None,
    do_file: InputPathType | None = None,
    do_draw_mask: str | None = None,
    fixed_do: str | None = None,
    mobile_do: str | None = None,
    key_press: str | None = None,
    viewer: str | None = None,
    anim_dup: float | None = None,
    save_as: str | None = None,
    save_index: float | None = None,
    save_range: str | None = None,
    save_last: bool = False,
    save_last_n: float | None = None,
    save_all: bool = False,
    echo_edu: bool = False,
    echo_nel_stdout: bool = False,
    echo_nel_stderr: bool = False,
    examples: bool = False,
    help_: bool = False,
    h: bool = False,
    help_nido: bool = False,
    c_demo: bool = False,
    viewer_cont: bool = False,
) -> DriveSumaParameters:
    """
    Build parameters.
    
    Args:
        command: Command to be sent to SUMA.
        surf_label: A label (identifier) to assign to the surface.
        surface_file: Name of surface file.
        surf_state: Name the state of that surface.
        surf_winding: Winding of triangles (ccw or cw).
        coordinates: A 1D formatted file containing new coordinates for nodes.
        autorecord: Set the autorecord prefix.
        background_color: Set the background color (R G B).
        view_file: Load a previously saved view file.
        do_file: Load a displayable object file.
        do_draw_mask: Restrict where DO node-based objects are displayed.
        fixed_do: Load a fixed coordinate type NIML DO.
        mobile_do: Mobile version of fixed_do.
        key_press: Act as if a key press was applied in the viewer.
        viewer: Specify which viewer should be acted upon.
        anim_dup: Save DUP copies of each frame into movie.
        save_as: Save image(s) in recorder in specified format.
        save_index: Save one image indexed IND.
        save_range: Save images from FROM to TO.
        save_last: Save last image.
        save_last_n: Save last N images.
        save_all: Save all images.
        echo_edu: Echoes the entire command line for edification purposes.
        echo_nel_stdout: Spit out the NIML object being sent to SUMA to stdout.
        echo_nel_stderr: Spit out the NIML object being sent to SUMA to stderr.
        examples: Show all the sample commands and exit.
        help_: Show the help in detail.
        h: Show help with slightly less detail.
        help_nido: Show the help for NIML Displayable Objects and exit.
        c_demo: Execute a preset number of commands to illustrate how one can\
            communicate with SUMA from one's own C code.
        viewer_cont: Apply settings to viewer or viewer controller.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "DriveSuma",
        "command": command,
        "save_last": save_last,
        "save_all": save_all,
        "echo_edu": echo_edu,
        "echo_nel_stdout": echo_nel_stdout,
        "echo_nel_stderr": echo_nel_stderr,
        "examples": examples,
        "help": help_,
        "h": h,
        "help_nido": help_nido,
        "c_demo": c_demo,
        "viewer_cont": viewer_cont,
    }
    if surf_label is not None:
        params["surf_label"] = surf_label
    if surface_file is not None:
        params["surface_file"] = surface_file
    if surf_state is not None:
        params["surf_state"] = surf_state
    if surf_winding is not None:
        params["surf_winding"] = surf_winding
    if coordinates is not None:
        params["coordinates"] = coordinates
    if autorecord is not None:
        params["autorecord"] = autorecord
    if background_color is not None:
        params["background_color"] = background_color
    if view_file is not None:
        params["view_file"] = view_file
    if do_file is not None:
        params["do_file"] = do_file
    if do_draw_mask is not None:
        params["do_draw_mask"] = do_draw_mask
    if fixed_do is not None:
        params["fixed_do"] = fixed_do
    if mobile_do is not None:
        params["mobile_do"] = mobile_do
    if key_press is not None:
        params["key_press"] = key_press
    if viewer is not None:
        params["viewer"] = viewer
    if anim_dup is not None:
        params["anim_dup"] = anim_dup
    if save_as is not None:
        params["save_as"] = save_as
    if save_index is not None:
        params["save_index"] = save_index
    if save_range is not None:
        params["save_range"] = save_range
    if save_last_n is not None:
        params["save_last_n"] = save_last_n
    return params


def drive_suma_cargs(
    params: DriveSumaParameters,
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
    cargs.append("DriveSuma")
    cargs.append(params.get("command"))
    if params.get("surf_label") is not None:
        cargs.extend([
            "-surf_label",
            params.get("surf_label")
        ])
    if params.get("surface_file") is not None:
        cargs.extend([
            "-i_TYPE",
            execution.input_file(params.get("surface_file"))
        ])
    if params.get("surf_state") is not None:
        cargs.extend([
            "-surf_state",
            params.get("surf_state")
        ])
    if params.get("surf_winding") is not None:
        cargs.extend([
            "-surf_winding",
            params.get("surf_winding")
        ])
    if params.get("coordinates") is not None:
        cargs.extend([
            "-xyz_1D",
            execution.input_file(params.get("coordinates"))
        ])
    if params.get("autorecord") is not None:
        cargs.extend([
            "-autorecord",
            params.get("autorecord")
        ])
    if params.get("background_color") is not None:
        cargs.extend([
            "-bkg_col",
            params.get("background_color")
        ])
    if params.get("view_file") is not None:
        cargs.extend([
            "-load_view",
            execution.input_file(params.get("view_file"))
        ])
    if params.get("do_file") is not None:
        cargs.extend([
            "-load_do",
            execution.input_file(params.get("do_file"))
        ])
    if params.get("do_draw_mask") is not None:
        cargs.extend([
            "-do_draw_mask",
            params.get("do_draw_mask")
        ])
    if params.get("fixed_do") is not None:
        cargs.extend([
            "-fixed_do",
            params.get("fixed_do")
        ])
    if params.get("mobile_do") is not None:
        cargs.extend([
            "-mobile_do",
            params.get("mobile_do")
        ])
    if params.get("key_press") is not None:
        cargs.extend([
            "-key",
            params.get("key_press")
        ])
    if params.get("viewer") is not None:
        cargs.extend([
            "-viewer",
            params.get("viewer")
        ])
    if params.get("anim_dup") is not None:
        cargs.extend([
            "-anim_dup",
            str(params.get("anim_dup"))
        ])
    if params.get("save_as") is not None:
        cargs.extend([
            "-save_as",
            params.get("save_as")
        ])
    if params.get("save_index") is not None:
        cargs.extend([
            "-save_index",
            str(params.get("save_index"))
        ])
    if params.get("save_range") is not None:
        cargs.extend([
            "-save_range",
            params.get("save_range")
        ])
    if params.get("save_last"):
        cargs.append("-save_last")
    if params.get("save_last_n") is not None:
        cargs.extend([
            "-save_last_n",
            str(params.get("save_last_n"))
        ])
    if params.get("save_all"):
        cargs.append("-save_all")
    if params.get("echo_edu"):
        cargs.append("-echo_edu")
    if params.get("echo_nel_stdout"):
        cargs.append("-echo_nel_stdout")
    if params.get("echo_nel_stderr"):
        cargs.append("-echo_nel_stderr")
    if params.get("examples"):
        cargs.append("-examples")
    if params.get("help"):
        cargs.append("-help")
    if params.get("h"):
        cargs.append("-h")
    if params.get("help_nido"):
        cargs.append("-help_nido")
    if params.get("c_demo"):
        cargs.append("-C_demo")
    if params.get("viewer_cont"):
        cargs.append("-com viewer_cont")
    return cargs


def drive_suma_outputs(
    params: DriveSumaParameters,
    execution: Execution,
) -> DriveSumaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DriveSumaOutputs(
        root=execution.output_file("."),
    )
    return ret


def drive_suma_execute(
    params: DriveSumaParameters,
    execution: Execution,
) -> DriveSumaOutputs:
    """
    A program to drive suma from the command line.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DriveSumaOutputs`).
    """
    params = execution.params(params)
    cargs = drive_suma_cargs(params, execution)
    ret = drive_suma_outputs(params, execution)
    execution.run(cargs)
    return ret


def drive_suma(
    command: str,
    surf_label: str | None = None,
    surface_file: InputPathType | None = None,
    surf_state: str | None = None,
    surf_winding: str | None = None,
    coordinates: InputPathType | None = None,
    autorecord: str | None = None,
    background_color: str | None = None,
    view_file: InputPathType | None = None,
    do_file: InputPathType | None = None,
    do_draw_mask: str | None = None,
    fixed_do: str | None = None,
    mobile_do: str | None = None,
    key_press: str | None = None,
    viewer: str | None = None,
    anim_dup: float | None = None,
    save_as: str | None = None,
    save_index: float | None = None,
    save_range: str | None = None,
    save_last: bool = False,
    save_last_n: float | None = None,
    save_all: bool = False,
    echo_edu: bool = False,
    echo_nel_stdout: bool = False,
    echo_nel_stderr: bool = False,
    examples: bool = False,
    help_: bool = False,
    h: bool = False,
    help_nido: bool = False,
    c_demo: bool = False,
    viewer_cont: bool = False,
    runner: Runner | None = None,
) -> DriveSumaOutputs:
    """
    A program to drive suma from the command line.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        command: Command to be sent to SUMA.
        surf_label: A label (identifier) to assign to the surface.
        surface_file: Name of surface file.
        surf_state: Name the state of that surface.
        surf_winding: Winding of triangles (ccw or cw).
        coordinates: A 1D formatted file containing new coordinates for nodes.
        autorecord: Set the autorecord prefix.
        background_color: Set the background color (R G B).
        view_file: Load a previously saved view file.
        do_file: Load a displayable object file.
        do_draw_mask: Restrict where DO node-based objects are displayed.
        fixed_do: Load a fixed coordinate type NIML DO.
        mobile_do: Mobile version of fixed_do.
        key_press: Act as if a key press was applied in the viewer.
        viewer: Specify which viewer should be acted upon.
        anim_dup: Save DUP copies of each frame into movie.
        save_as: Save image(s) in recorder in specified format.
        save_index: Save one image indexed IND.
        save_range: Save images from FROM to TO.
        save_last: Save last image.
        save_last_n: Save last N images.
        save_all: Save all images.
        echo_edu: Echoes the entire command line for edification purposes.
        echo_nel_stdout: Spit out the NIML object being sent to SUMA to stdout.
        echo_nel_stderr: Spit out the NIML object being sent to SUMA to stderr.
        examples: Show all the sample commands and exit.
        help_: Show the help in detail.
        h: Show help with slightly less detail.
        help_nido: Show the help for NIML Displayable Objects and exit.
        c_demo: Execute a preset number of commands to illustrate how one can\
            communicate with SUMA from one's own C code.
        viewer_cont: Apply settings to viewer or viewer controller.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DriveSumaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DRIVE_SUMA_METADATA)
    params = drive_suma_params(
        command=command,
        surf_label=surf_label,
        surface_file=surface_file,
        surf_state=surf_state,
        surf_winding=surf_winding,
        coordinates=coordinates,
        autorecord=autorecord,
        background_color=background_color,
        view_file=view_file,
        do_file=do_file,
        do_draw_mask=do_draw_mask,
        fixed_do=fixed_do,
        mobile_do=mobile_do,
        key_press=key_press,
        viewer=viewer,
        anim_dup=anim_dup,
        save_as=save_as,
        save_index=save_index,
        save_range=save_range,
        save_last=save_last,
        save_last_n=save_last_n,
        save_all=save_all,
        echo_edu=echo_edu,
        echo_nel_stdout=echo_nel_stdout,
        echo_nel_stderr=echo_nel_stderr,
        examples=examples,
        help_=help_,
        h=h,
        help_nido=help_nido,
        c_demo=c_demo,
        viewer_cont=viewer_cont,
    )
    return drive_suma_execute(params, execution)


__all__ = [
    "DRIVE_SUMA_METADATA",
    "DriveSumaOutputs",
    "DriveSumaParameters",
    "drive_suma",
    "drive_suma_params",
]
